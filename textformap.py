def text():
                #bySoby
                t = bs.newNode('text',
                       attrs={ 'text':'this is how u jump to second line and say\nto not make it long line',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0: 0.0,500: 1.0,4500: 1.0,5000: 0.0})
                bs.gameTimer(5000,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue043message 2 showing how to add \ue043icons\nif u need that\ue043',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{9000: 0.0,9500: 1.0,13500: 1.0,14000: 0.0})
                bs.gameTimer(14000,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'message 3do not forget to subscribe to\nBOMBSQUAD FOCUS',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{17500: 0.0,18000: 1.0,22000: 1.0,22500: 0.0})
                bs.gameTimer(22500,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'message 4edit these msgs as per ur choice',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{26500: 0.0,27000: 1.0,31000: 1.0,31500: 0.0})
                bs.gameTimer(31500,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'message 5 edit it too',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{35500: 0.0,36000: 1.0,40000: 1.0,40500: 0.0})
                bs.gameTimer(40500,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'You Mes6sage',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{44500: 0.0,45000: 1.0,49000: 1.0,49500: 0.0})
                bs.gameTimer(49500,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'You Mes7sage',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{55000: 0.0,55500: 1.0,59500: 1.0,60000: 0.0})
                bs.gameTimer(60000,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'You Mes8sage',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,137),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{64000: 0.0,64500: 1.0,68500: 1.0,69000: 0.0})
                bs.gameTimer(69000,t.delete)
        bs.gameTimer(3500,bs.Call(text))
        bs.gameTimer(73000,bs.Call(text),repeat = True)
#check the video how u can paste and where to paste