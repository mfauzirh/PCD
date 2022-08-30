import PySimpleGUI as sg
import os.path
import program as pcd    

def make_win1():
    main_menu = [
    [
        sg.Button("Extract RGB From Image", size=(40, 1))
    ],
    [
        sg.Button("Convert Image To Grayscale", size=(40, 1))
    ],
    [
        sg.Button("Detect Circle", size=(40, 1))
    ],
    [
        sg.Button("Exit", size=(40, 1))
    ],
]
    return sg.Window('Aplikasi Pengelolahan Citra Digital (PCD)', main_menu, location=(800,600), finalize=True)

def make_win2():
    extract_rgb = [
        [
            sg.In(size=(130, 1), enable_events=True, key="-PATHEXRGB-"),
            sg.FileBrowse(),  
        ],
        [
            sg.Text("RGB Channel dari citra yang dipilih:"),
        ],
        [
            sg.Text("Red Channel"),
            sg.Listbox(
                values=[], enable_events=True, size=(30, 15), key="-R-"
            ),
            sg.Text("Green Channel"),
            sg.Listbox(
                values=[], enable_events=True, size=(30, 15), key="-G-"
            ),
            sg.Text("Blue Channel"),
            sg.Listbox(
                values=[], enable_events=True, size=(30, 15), key="-B-"
            )
        ],
        [
            sg.Button("Kembali", size=(120, 1))
        ]
    ]

    return sg.Window('Aplikasi Pengelolahan Citra Digital (PCD) - Extract RGB', extract_rgb, finalize=True)

def make_win3():
    convert_to_grayscale = [
        [
            sg.In(size=(25, 1), enable_events=True, key="-PATHGSL-"),
            sg.FileBrowse(key="-FILEBROWSERGSL-"),  
        ],
        [
            sg.Text("RGB Channel dari citra yang telah diconvert ke grayscale:"),
        ],
        [
            sg.Text("Red Channel"),
            sg.Listbox(
                values=[], enable_events=True, size=(30, 15), key="-RGSL-"
            ),
            sg.Text("Green Channel"),
            sg.Listbox(
                values=[], enable_events=True, size=(30, 15), key="-GGSL-"
            ),
            sg.Text("Blue Channel"),
            sg.Listbox(
                values=[], enable_events=True, size=(30, 15), key="-BGSL-"
            )
        ],
        [
            sg.Button("Kembali", size=(40, 1))
        ]
    ]

    return sg.Window('Aplikasi Pengelolahan Citra Digital (PCD) - Grayscale Converter', convert_to_grayscale, finalize=True)

window1, window2, window3 = make_win1(), None, None

while True:         
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Kembali':
        window.close()
        if window == window3:
            window3 = None
        if window == window2:     
            window2 = None
        elif window == window1:    
            break

    elif event == 'Extract RGB From Image' and not window2:
        window2 = make_win2()

    elif event == 'Convert Image To Grayscale' and not window3:
        window3 = make_win3()

    elif event == 'Detect Circle':
        path = 'assets/images/lingkaran.jpg'

        img = pcd.readImage(path)
        pcd.showImage(img, "Original")

        img = pcd.detectCircleByColor(img, 0)
        pcd.showImage(img, "Detected")

    elif event == '-PATHEXRGB-':
        path = values["-PATHEXRGB-"]

        img = pcd.readImage(path)

        [R, G, B] = pcd.extractRGB(img)

        window2["-R-"].update(R)
        window2["-G-"].update(G)
        window2["-B-"].update(B)

        pcd.showImage(img, "Original")

    elif event == '-PATHGSL-':
        path = values["-PATHGSL-"]

        img = pcd.readImage(path)

        pcd.showImage(img, "Original")

        grayscale = pcd.weightedAverageGrayscale(img)
        [R, G, B] = pcd.extractRGB(grayscale)
        window3["-RGSL-"].update(R)
        window3["-GGSL-"].update(G)
        window3["-BGSL-"].update(B)
        pcd.showImage(grayscale, "Converted To Grayscale")

window.close()