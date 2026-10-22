# 005abeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](005abeac.md)

## 関数情報

~~~json
{
  "address": "005abeac",
  "name": "FUN_005abeac",
  "size": 768,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1db95761b60b05a5a346c6965ee37987dfdaa6481cf3f4b1c6b70bff6549a8a5",
  "source_text_sha256": "1db95761b60b05a5a346c6965ee37987dfdaa6481cf3f4b1c6b70bff6549a8a5"
}
~~~
## 呼び出し元

- [005a9c58](../005a9/005a9c58.md)
- [005ae770](../005ae/005ae770.md)

## 呼び出し先

- [005abb94](../005ab/005abb94.md)
- [005ac1ac](../005ac/005ac1ac.md)
- [00bdd890](../00bdd/00bdd890.md)

## 疑似コード 1/1 / UTF-8 5818 bytes

~~~c

byte * FUN_005abeac(long param_1,byte *param_2,byte *param_3,
                   basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
                   *param_4)

{
  byte bVar1;
  ulong uVar2;
  uint uVar3;
  char cVar4;
  uint uVar5;
  char cVar6;
  
  if (param_2 == param_3) {
    return param_2;
  }
  bVar1 = *param_2;
  uVar2 = (ulong)bVar1;
  if (bVar1 < 0x72) {
    if (bVar1 < 0x66) {
      if (bVar1 == 0x30) {
        if (param_4 !=
            (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0) {
          std::__ndk1::
          basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::operator=
                    (param_4,'\0');
          goto LAB_005ac194;
        }
        uVar2 = 0;
      }
      else {
        if (bVar1 == 99) {
          if ((param_2 + 1 != param_3) && (bVar1 = param_2[1], (byte)((bVar1 & 0xdf) + 0xbf) < 0x1a)
             ) {
            if (param_4 !=
                (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
                0x0) {
              std::__ndk1::
              basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
              operator=(param_4,bVar1 & 0x1f);
              return param_2 + 2;
            }
            FUN_005ac1ac();
            return param_2 + 2;
          }
          goto LAB_005ac1a8;
        }
        if (bVar1 == 0x5f) goto LAB_005ac1a8;
LAB_005ac168:
        if ((-1 < (char)bVar1) &&
           ((*(ulong *)(*(long *)(*(long *)(param_1 + 8) + 0x10) + uVar2 * 8) & 0x60) != 0))
        goto LAB_005ac1a8;
        if (param_4 !=
            (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0) {
          std::__ndk1::
          basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::operator=
                    (param_4,bVar1);
          goto LAB_005ac194;
        }
      }
    }
    else if (bVar1 == 0x66) {
      if (param_4 !=
          (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0) {
        std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
        ::operator=(param_4,'\f');
        goto LAB_005ac194;
      }
      uVar2 = 0xc;
    }
    else {
      if (bVar1 != 0x6e) goto LAB_005ac168;
      if (param_4 !=
          (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0) {
        std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
        ::operator=(param_4,'\n');
        goto LAB_005ac194;
      }
      uVar2 = 10;
    }
  }
  else {
    if (0x74 < bVar1) {
      if (bVar1 == 0x75) {
        if ((param_2 + 1 == param_3) ||
           ((((bVar1 = param_2[1], (bVar1 & 0xf8) != 0x30 && ((bVar1 & 0xfe) != 0x38)) &&
             (5 < (bVar1 | 0x20) - 0x61)) || (param_2 = param_2 + 2, param_2 == param_3))))
        goto LAB_005ac1a8;
        bVar1 = *param_2;
        if ((((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) && (5 < (bVar1 | 0x20) - 0x61))
        goto LAB_005ac1a8;
      }
      else {
        if (bVar1 == 0x76) {
          if (param_4 !=
              (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0)
          {
            std::__ndk1::
            basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
            operator=(param_4,'\v');
            goto LAB_005ac194;
          }
          uVar2 = 0xb;
          goto LAB_005ac190;
        }
        if (bVar1 != 0x78) goto LAB_005ac168;
      }
      if (param_2 + 1 != param_3) {
        bVar1 = param_2[1];
        uVar3 = (uint)bVar1;
        cVar4 = '\0';
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar3 = uVar3 | 0x20;
          if (5 < uVar3 - 0x61) goto LAB_005ac1a8;
          cVar4 = -0x57;
        }
        if (param_2 + 2 != param_3) {
          bVar1 = param_2[2];
          uVar5 = (uint)bVar1;
          cVar6 = -0x30;
          if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
            uVar5 = uVar5 | 0x20;
            if (5 < uVar5 - 0x61) goto LAB_005ac1a8;
            cVar6 = -0x57;
          }
          if (param_4 !=
              (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0)
          {
            std::__ndk1::
            basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
            operator=(param_4,cVar6 + (char)uVar5 + (cVar4 + (char)uVar3) * '\x10');
            return param_2 + 3;
          }
          FUN_005ac1ac();
          return param_2 + 3;
        }
      }
LAB_005ac1a8:
                    /* WARNING: Subroutine does not return */
      FUN_005abb94();
    }
    if (bVar1 == 0x72) {
      if (param_4 !=
          (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0) {
        std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
        ::operator=(param_4,'\r');
        goto LAB_005ac194;
      }
      uVar2 = 0xd;
    }
    else {
      if (bVar1 != 0x74) goto LAB_005ac168;
      if (param_4 !=
          (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0) {
        std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
        ::operator=(param_4,'\t');
        goto LAB_005ac194;
      }
      uVar2 = 9;
    }
  }
LAB_005ac190:
  FUN_005ac1ac(param_1,uVar2);
LAB_005ac194:
  return param_2 + 1;
}

~~~
