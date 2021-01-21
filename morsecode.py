# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = False
    answer = ["H", "HELP"]
    user_input = user_input.upper()

    if user_input in answer:
        result = True

    return result
    # ==================================


def is_validated_english_sentence(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
          3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_english_sentence("Hello 123")
        False
        >>> mc.is_validated_english_sentence("Hi!")
        True
        >>> mc.is_validated_english_sentence(".!.")
        False
        >>> mc.is_validated_english_sentence("!.!")
        False
        >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = True
    case_2 = "_@#$%^&*()-+=[]{}\"\';:\|`~"
    case_3 = ".,!? "
    cnt = 0

    for ch in user_input:
        # case 1) 숫자 포함
        # if ch.isdigit():
        #     result = False
        #     break
        if ch >= '0' and ch <= '9':
            result = False
            break

        # case 2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함
        if ch in case_2:
            result = False
            break

        # case 3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
        if ch in case_3:
            cnt += 1

    if cnt == len(user_input):
        result = False

    return result
    # ==================================


def is_validated_morse_code(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_morse_code("..")
        True
        >>> mc.is_validated_morse_code("..-")
        True
        >>> mc.is_validated_morse_code("..-..")
        False
        >>> mc.is_validated_morse_code(". . . .")
        True
        >>> mc.is_validated_morse_code("-- -- -- --")
        True
        >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = True
    case_1 = "-. "
    case_2 = get_morse_code_dict().values()

    # case 1) "-","."," "외 다른 글자가 포함되어 있는 경우
    for ch in user_input:
        if ch not in case_1:
            result = False
            break

    # case 2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우
    morse_input = user_input.split(' ')
    for i in morse_input:
        if i not in case_2:
            result = False
            break

    return result
    # ==================================



def get_cleaned_english_sentence(raw_english_sentence):
    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        >>> import morsecode as mc
        >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = ""
    case_1 = ".,!?"

    # 1) 4개의 문장부호를 ".,!?" 삭제
    for ch in raw_english_sentence:
        if ch not in case_1:
            result += ch

    # 2) 양쪽끝 여백을 제거
    result = result.strip(' ')

    return result
    # ==================================


def decoding_character(morse_character):
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_character("-")
        'T'
        >>> mc.decoding_character(".")
        'E'
        >>> mc.decoding_character(".-")
        'A'
        >>> mc.decoding_character("...")
        'S'
        >>> mc.decoding_character("....")
        'H'
        >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    result = None

    for k, v in morse_code_dict.items():
        if v == morse_character:  # value 값과 입력값이 같으면 
            result = k         # 해당 key 값을 리턴
            break

    return result
    # ==================================


def encoding_character(english_character):
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_character("G")
        '--.'
        >>> mc.encoding_character("A")
        '.-'
        >>> mc.encoding_character("C")
        '-.-.'
        >>> mc.encoding_character("H")
        '....'
        >>> mc.encoding_character("O")
        '---'
        >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    result = None

    # decoding_character와 동일한 방법
    for k, v in morse_code_dict.items():
        if k == english_character:
            result = v
            break

    return result
    # ==================================


def decoding_sentence(morse_sentence):
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = None
    ch_list = []  # decoding된 문자 하나하나를 담는 list
    morse_list = morse_sentence.strip().split(' ') # 입력 문장 양 끝 공백 지우고, 한 칸만 split!
                                                   # 참고로 그냥 split()하면 공백 2칸인 경우도 다 지워진다.
                                                   # 이게 필요한 이유는 띄어쓰기를 넣어야 하기 때문

    for morse in morse_list:
        if is_validated_morse_code(morse):  # 1. 입력 모스부호가 변환 가능한지 먼저 검증
            ch_list.append(decoding_character(morse)) # 문자로 디코딩하여 list에 넣는다.
        
        # 2. 띄어쓰기를 넣어주기 위해, 입력 리스트에 ''된 값을 띄어쓰기로 넣어준다.
        if morse == '':
            ch_list.append(' ')
    
    result = "".join(ch_list)

    return result
    # ==================================


def encoding_sentence(english_sentence):
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = None
    if not is_validated_english_sentence(english_sentence):
        return result
    
    words_list = get_cleaned_english_sentence(english_sentence).split()
    morse_list = []

    for sen in words_list:
        for ch in sen.upper():
            morse_list.append(encoding_character(ch))
        morse_list.append('')

    result = " ".join(morse_list)[:-1]

    return result
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============

    # 입력: 모스부호, 출력: 문자
    # 입력: 문자, 출력: 모스부호

    while True:
        order = input("Input your message(H - Help, 0 - Exit): ")
        
        #1. 0 입력하면 종료
        if order == '0':
            break

        #2. 사용자가 대소문자에 상관없이 "h"또는 "help"를 입력하면 get_help_message 함수를 호출
        elif is_help_command(order):
            print(get_help_message())

        #3. 모스부호로 변환이 가능한 알파벳 문장이 입력되면 모스부호로 변환된 값이 출력
        elif is_validated_english_sentence(order):
            print(encoding_sentence(order))

        elif decoding_sentence(order):
            print(decoding_sentence(order))

        else:
            morse = decoding_sentence(order)
            
            #4. 알파벳으로 변환이 가능한 모스부호가 입력되면 알파벳으로 변환
            if morse:
                print(morse)

            #5. 변환이 불가능한 입력에 한해서는 에러 메세지를 출력
            else:
                print("Wrong Input")

    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
