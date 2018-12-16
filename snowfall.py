def snowfall():
                p = (-10+(random.random()*30),15,-10+(random.random()*30))
                v = ((-5.0+random.random()*30.0) * (-1.0 if p[0] > 0 else 1.0), -50.0,(-5.0+random.random()*30.0) * (-1.0 if p[0] > 0 else 1.0))
                bs.emitBGDynamics(position=p,velocity=v,count=10,scale=1+random.random(),spread=0,chunkType='spark')
        
        bs.gameTimer(20,bs.Call(snowfall),repeat = True)