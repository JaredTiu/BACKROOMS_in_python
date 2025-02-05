maze = [[(0, 0), (40, 0)], [(0, 40), (40, 40)], [(0, 0), (0, 40)], 
        [(40, 0), (80, 0)], [(40, 40), (80, 40)], [(80, 0), (120, 0)], 
        [(120, 0), (120, 40)], [(120, 0), (160, 0)], [(120, 40), (160, 40)], 
        [(160, 0), (200, 0)], [(200, 0), (240, 0)], [(200, 40), (240, 40)], 
        [(240, 0), (280, 0)], [(280, 0), (320, 0)], [(320, 0), (320, 40)], 
        [(320, 0), (360, 0)], [(360, 0), (400, 0)], [(360, 40), (400, 40)], 
        [(400, 0), (440, 0)], [(400, 40), (440, 40)], [(440, 0), (480, 0)], 
        [(440, 40), (480, 40)], [(480, 0), (520, 0)], [(520, 0), (560, 0)], 
        [(560, 0), (560, 40)], [(560, 0), (600, 0)], [(600, 0), (600, 40)], 
        [(0, 40), (0, 80)], [(40, 80), (80, 80)], [(80, 40), (80, 80)], 
        [(80, 80), (120, 80)], [(160, 40), (160, 80)], [(200, 40), (200, 80)], 
        [(240, 40), (240, 80)], [(280, 40), (280, 80)], [(320, 40), (320, 80)], 
        [(360, 40), (360, 80)], [(400, 80), (440, 80)], [(440, 80), (480, 80)], 
        [(480, 80), (520, 80)], [(520, 40), (520, 80)], [(560, 40), (560, 80)], 
        [(600, 40), (600, 80)], [(0, 80), (0, 120)], [(40, 120), (80, 120)], 
        [(80, 120), (120, 120)], [(120, 120), (160, 120)], [(160, 80), (160, 120)], 
        [(160, 120), (200, 120)], [(240, 80), (240, 120)], [(280, 80), (280, 120)], 
        [(320, 80), (320, 120)], [(320, 120), (360, 120)], [(360, 80), (360, 120)], 
        [(400, 80), (400, 120)], [(440, 120), (480, 120)], [(480, 120), (520, 120)], 
        [(520, 120), (560, 120)], [(560, 120), (600, 120)], [(600, 80), (600, 120)], 
        [(0, 160), (40, 160)], [(0, 120), (0, 160)], [(40, 160), (80, 160)], [(80, 160), (120, 160)], 
        [(160, 120), (160, 160)], [(200, 120), (200, 160)], [(240, 120), (240, 160)], 
        [(280, 120), (280, 160)], [(280, 160), (320, 160)], [(320, 160), (360, 160)], 
        [(400, 120), (400, 160)], [(400, 160), (440, 160)], [(440, 120), (440, 160)], 
        [(480, 160), (520, 160)], [(520, 160), (560, 160)], [(600, 120), (600, 160)], 
        [(0, 200), (40, 200)], [(0, 160), (0, 200)], [(80, 200), (120, 200)], [(120, 160), (120, 200)], 
        [(160, 160), (160, 200)], [(200, 200), (240, 200)], [(240, 160), (240, 200)], 
        [(240, 200), (280, 200)], [(280, 200), (320, 200)], [(360, 160), (360, 200)], 
        [(360, 200), (400, 200)], [(400, 160), (400, 200)], [(440, 200), (480, 200)], 
        [(480, 160), (480, 200)], [(520, 200), (560, 200)], [(560, 160), (560, 200)], 
        [(600, 160), (600, 200)], [(0, 200), (0, 240)], [(40, 240), (80, 240)], [(80, 200), (80, 240)], 
        [(120, 240), (160, 240)], [(160, 200), (160, 240)], [(160, 240), (200, 240)], 
        [(200, 240), (240, 240)], [(240, 240), (280, 240)], [(320, 200), (320, 240)], 
        [(360, 200), (360, 240)], [(400, 240), (440, 240)], [(440, 200), (440, 240)], 
        [(440, 240), (480, 240)], [(520, 200), (520, 240)], [(600, 200), (600, 240)], 
        [(0, 240), (0, 280)], [(40, 240), (40, 280)], [(80, 280), (120, 280)], [(120, 240), (120, 280)], 
        [(160, 280), (200, 280)], [(200, 280), (240, 280)], [(280, 240), (280, 280)], 
        [(320, 240), (320, 280)], [(360, 240), (360, 280)], [(400, 240), (400, 280)], 
        [(440, 280), (480, 280)], [(480, 280), (520, 280)], [(520, 240), (520, 280)], 
        [(560, 240), (560, 280)], [(600, 240), (600, 280)], [(0, 280), (0, 320)], [(40, 280), (40, 320)], 
        [(40, 320), (80, 320)], [(80, 320), (120, 320)], [(120, 320), (160, 320)], 
        [(160, 280), (160, 320)], [(200, 280), (200, 320)], [(240, 320), (280, 320)], 
        [(280, 280), (280, 320)], [(320, 280), (320, 320)], [(320, 320), (360, 320)], 
        [(360, 320), (400, 320)], [(400, 320), (440, 320)], [(440, 280), (440, 320)], 
        [(480, 320), (520, 320)], [(520, 320), (560, 320)], [(560, 280), (560, 320)], 
        [(600, 280), (600, 320)], [(0, 320), (0, 360)], [(40, 320), (40, 360)], [(80, 360), (120, 360)], 
        [(120, 360), (160, 360)], [(160, 360), (200, 360)], [(200, 360), (240, 360)], 
        [(240, 320), (240, 360)], [(240, 360), (280, 360)], [(280, 360), (320, 360)], 
        [(320, 360), (360, 360)], [(360, 320), (360, 360)], [(440, 320), (440, 360)], 
        [(440, 360), (480, 360)], [(480, 360), (520, 360)], [(560, 320), (560, 360)], 
        [(600, 320), (600, 360)], [(0, 400), (40, 400)], [(0, 360), (0, 400)], [(40, 400), (80, 400)], 
        [(80, 400), (120, 400)], [(120, 400), (160, 400)], [(160, 400), (200, 400)], 
        [(200, 400), (240, 400)], [(240, 400), (280, 400)], [(280, 400), (320, 400)], 
        [(320, 400), (360, 400)], [(360, 400), (400, 400)], [(400, 360), (400, 400)], 
        [(400, 400), (440, 400)], [(440, 400), (480, 400)], [(480, 400), (520, 400)], 
        [(520, 400), (560, 400)], [(560, 360), (560, 400)], [(560, 400), (600, 400)], [(600, 360), (600, 400)]]