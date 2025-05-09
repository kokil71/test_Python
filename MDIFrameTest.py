import wx

class MDIFrame(wx.MDIParentFrame):
    def __init__(self, parent):
        # 수퍼클래스인 MDIParentFrame을 초기화 시킨다
        wx.MDIParentFrame.__init__(self,parent, -1,'MDI Parent Window', size=(800,600))

        # File 메뉴의 하위 메뉴 생성
        filemenu = wx.Menu()
        filemenu.Append(100, "New Window")
        filemenu.Append(200, "Exit")

        # 메뉴바 생성 후 File 메뉴 붙이기
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")

        # MDI 프레임에 메뉴바를 연결
        self.SetMenuBar(menubar)

        # 메뉴 아이템 클릭시 동작함수 바인딩
        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=100)
        self.Bind(wx.EVT_MENU, self.OnExit, id=200)

        # Frame 화면 중앙에 놓기
        self.Center()

    # 종료
    def OnExit(self, evt):
        self.Close(True)

    # New Window 메뉴 아이템 클릭시 동작
    def OnNewWindow(self, evt):

        """""""""""""""""""""""""""""
        숫자만 입력 가능한 Text Ctrl 제작 
        """""""""""""""""""""""""""""
        class NumberTextCtrl(wx.TextCtrl):
            def __init__(self, parent, id, value):
                wx.TextCtrl.__init__(self, parent, id, value, pos=wx.DefaultPosition, size=(100,-1))
                # 키보드 눌림 이벤트 바인딩
                # wx.EVT_CHAR도 가능합니다!!
                self.Bind(wx.EVT_KEY_DOWN, self.handle_keypress)

            # 키보드 입력시 동작: 숫자만 입력 가능하게
            def handle_keypress(self, event):
                # 눌린 키의 키코드 값
                keycode = event.GetKeyCode()
                if chr(keycode).isnumeric():
                    # 이벤트 스킵
                    event.Skip(skip=True)
                # 백스페이스, DEL, 화살표 키도 입력 가능하도록 이벤트에서 제외.
                if keycode in [8, 127, 314, 315, 316, 317]:
                    event.Skip(skip=True)

        # 윈도우 사이즈 입력 대화상자 : wx.Dialog를 상속받아 만듭니다
        class GetWindowSizeDialog(wx.Dialog):
            def __init__(self, parent, id=wx.ID_ANY, title="", label="",
                         pos=wx.DefaultPosition, size=wx.DefaultSize):
                wx.Dialog.__init__(self, parent, id, title, pos, size)
                self.panel = wx.Panel(self, -1)

                # 대화상자 메시지
                self.message = wx.StaticText(self.panel, label=label)
                # 창 크기 x, y 값 : 숫자만 입력가능
                self.xvalue = NumberTextCtrl(self.panel, -1, "300")
                self.yvalue = NumberTextCtrl(self.panel, -1, "250")
                # OK 버튼
                self.btnOK = wx.Button(self.panel,-1, "OK")

                # 수직 박스사이저
                bsizer = wx.BoxSizer(wx.VERTICAL)
                # 수평 박스사이저
                hsizer = wx.BoxSizer(wx.HORIZONTAL)
                bsizer.Add(self.message,0, wx.ALL|wx.ALIGN_CENTER, 20)
                hsizer.Add(self.xvalue,0, wx.ALL|wx.ALIGN_CENTER, 10)
                hsizer.Add(self.yvalue,0, wx.ALL|wx.ALIGN_CENTER, 10)
                bsizer.Add(hsizer, 0, wx.ALL|wx.ALIGN_CENTER, 10)
                bsizer.Add(self.btnOK, 0, wx.ALL|wx.ALIGN_CENTER, 10)
                self.panel.SetSizer(bsizer)

                self.Bind(wx.EVT_BUTTON, self.ok_pressed, self.btnOK)

            # OK가 눌렸을 때 동작
            def ok_pressed(self, event):
                if self.IsModal():
                    self.EndModal(wx.ID_OK)
                else:
                    self.Close()

            # 창 크기 (x,y)값 출력
            def GetValue(self):
                return (int(self.xvalue.GetValue()), int(self.yvalue.GetValue()))


        modal = GetWindowSizeDialog(None, -1, title="MDI Child Frame 사이즈 입력",
                                    label="MDI Child Frame을 추가합니다.\n창크기를 입력하세요.")


        # # OK를 클릭하면 동작
        if modal.ShowModal() == wx.ID_OK:
            # 사용자가 입력한 값 얻기
            winx,winy = modal.GetValue()

            # MDI Child Frame 생성
            win = wx.MDIChildFrame(self, -1, "Child Window", size=(winx,winy))

            # MDI Child Frame 내부 GUI
            win.panel = wx.Panel(win, -1)
            win.st = wx.StaticText(win, -1, "입력한 창 크기: ("+str(winx)+", "+str(winy)+")")
            win.bsizer = wx.BoxSizer(wx.HORIZONTAL)
            win.bsizer.Add(win.st, 0, wx.ALL, 30)
            win.SetSizer(win.bsizer)
            win.Show(True)



if __name__=="__main__":
    app = wx.App()
    frame = MDIFrame(parent=None)
    frame.Show()
    app.MainLoop()