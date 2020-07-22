from guizero import App, Box, PushButton,ButtonGroup, ListBox, Slider

display_width = 1920
display_height = 1080

class interface:

    def __init__(self):
        self.screen = App(title="Camera", width=display_width, height=display_height)
        self.screen.full_screen=False

        self.sideBar = Box(self.screen,height="fill",width= display_width*0.20,align="right")
        self.topBar = Box(self.screen, width="fill",height= display_height*0.1,align="top")
        
        #Side-bar components 
        self.preview = PushButton(self.sideBar, width=128, height=128,text="Video", image="icons/preview.png", command=self.preview)
        self.captureImage = PushButton(self.sideBar, width=128, height=128, text="Image", image="icons/photo.png")
        self.captureVideo = PushButton(self.sideBar, width=128, height=128,text="Video", image="icons/video.png")
        self.imageSettings = PushButton(self.sideBar, width=128, height=128,text="Video", image="icons/image_settings.png", command=self.imageSettings)
        self.videoSettings = PushButton(self.sideBar, width=128, height=128,text="Video", image="icons/video_settings.png")
        self.settings = PushButton(self.sideBar, width=128, height=128,text="Video", image="icons/settings.png")

        #Image settings box components
        self.imageSettingsBox = Box(self.screen, height=500, width=500, border=True,visible=False)
        self.SSSelector = ListBox(self.imageSettingsBox,items=[1/4,1/2,300,400,500,600,700,800], command=self.updateISO)
        self.ISOSlider = Slider(self.imageSettingsBox, start=100, end=800,width="fill", height=100)
        self.screen.display()

    def updateISO(self,value):
        print(value)
    def imageSettings(self):
        self.imageSettingsBox.visible = True

    def preview(self):
        self.imageSettingsBox.visible = False
if __name__ == '__main__':
    newInterface = interface()