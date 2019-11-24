from marker_creation import marker_creation
from marker_recognition import marker_recognition
from marker_recognition import ScalingMode
from select_target import select_target
from moving_direction import moving_dir
from turning_direction import turning_dir

## Constants
ARUCO_CODE_ID = 70
INPUT_IMG = 'img9.jpg'
mode = ScalingMode.FIX_SIZE

#marker_creation(ARUCO_CODE_ID)

ids, corners = marker_recognition(INPUT_IMG, mode)
targetCorners = select_target(ids, corners, ARUCO_CODE_ID)

## az alap ötletem az hogy ha el van fordulva a kód, tehát nem szembe állunk vele, akkor az egyes sarkok koordinátái 
# más-más magasságokban lesznek. pl ha a bal felső sarok magasabban van mint a jobb felső sarok, akkor az azt jelenti, 
# hogy a kódra 'jobbról nézünk rá'
# emellett ha a bal felső és jobb felső sarok közötti magasságkülönbség kisebb mint a bal alsó és jobb alsó sarok 
# közöti magasságkülönbség, akkor azt is tudjuk hogy a kód hozzánk képest lefelé van
# vagyis meg tudtuk mondani, hogy a látott kódtól jobbra vagyunk és alattunk van -> balra le kell navigálni.

# ha sikerüt úgy beállnia a drónnak, hogy valószínűleg szembeállunk vele (nincs számottevő különbség az Y koordinátákban)
# akkor úgy kell navigálnunk, hogy a kód a kép közepére kerüljön.

turning_dir()
moving_dir()

