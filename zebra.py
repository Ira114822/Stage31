class Lines:

    black = "black line"
    white = "white line"
    first_line = black

    def get_stripe(self):
        if self.first_line == self.black:
            return self.white
        return self.black

    def zebra(self):
        print(Lines.black)

        for i in range(0, 10):
            strip = self.get_stripe()
            print(strip)
            self.first_line = strip

zebra = Lines()
zebra.zebra()


