class Television:

    maxChannel = 999;
    maxVolume = 100;
    def __init__(self,brand,model):
        if not isinstance(brand, str):
            raise TypeError('brand must be string')
        if not isinstance(model, str):
            raise TypeError('model must be string')
        
        self._brand = brand
        self._model = model
        self._powerOn = False
        self._volume = 50
        self._muted = False
        self._channel = 1
        self._prevChan = 1

    def togglePower(self):
        if self._powerOn == True:
            self._powerOn = False
        else:
            self._powerOn = True

    def volumeUp(self):             
        if self._powerOn == True:
            if self._volume < self.maxVolume:
                self._volume += 1

    def volumeDown(self):           
        if self._powerOn == True:
            if self._volume > 0:
                self._volume -= 1

    def toggleMute(self):
        if self._powerOn == True:
            if self._muted == False:
                self._muted = True
            else:
                self._muted = False
   
    def channelUp(self):            
        if self._powerOn == True:
            self._prevChan = self._channel
            self._channel = (self._channel+1)%self.maxChannel
            
    def channelDown(self):
        if self._powerOn == True:
            self._prevChan = self._channel
            self._channel = ((self._channel-2)%(self.maxChannel))+1

    def setChannel(self, number):
        if self._powerOn == True:
            self._prevChan = self._channel
            if number < 1:
                self._channel = 1
            elif number > self.maxChannel:
                self._channel = self.maxChannel
            else:
                self._channel = number 

    def jumpPrevChan(self):
        if self._powerOn == True:
            self._prevChan, self._channel = self._channel, self._prevChan
    def __str__(self):
        return f'\n  Television:\nBrand:\t\t{self._brand!s}\nModel:\t\t{self._model!s}\nPower:\t\t{self._powerOn!s}\nVolume:\t\t{self._volume!s}\nMuted:\t\t{self._muted!s}\nChannel:\t{self._channel!s}\nPrevChannel:\t{self._prevChan!s}\n\n'
    

if __name__ == '__main__':
    telly = Television('FukuShiba','Super SBOLED')
    print('--- init ---',telly)
    telly.channelUp()
    telly.volumeDown()
    print("--- chanUp, volDown (but it's turned off) ---",telly)
    telly.togglePower()
    telly.channelUp()
    telly.volumeUp()
    print('--- togglePower, chanUp, volUp ---',telly)
    telly.toggleMute()
    telly.setChannel(59)
    telly.volumeDown()
    telly.volumeDown()
    print('--- toggleMute, setChan(59), volDown, volDown ---',telly)
    telly.jumpPrevChan()
    telly.channelDown()
    print('--- prevChan, chanDown ---',telly)
