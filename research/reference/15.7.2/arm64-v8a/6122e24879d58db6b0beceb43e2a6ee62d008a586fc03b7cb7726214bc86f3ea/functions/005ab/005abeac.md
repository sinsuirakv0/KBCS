# 005abeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `005abeac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "aaef458c7f5e427e9e86cbb4dd55b898aa2b1c9ffa848bd4505a9b873d039697",
  "source_text_sha256": "aaef458c7f5e427e9e86cbb4dd55b898aa2b1c9ffa848bd4505a9b873d039697"
}
~~~

## 呼び出し元

- [005a9c58](../005a9/005a9c58.md)
- [005ae770](../005ae/005ae770.md)

## 呼び出し先

- [005abb94](../005ab/005abb94.md)
- [005ac1ac](../005ac/005ac1ac.md)
- [00bdd890](../00bdd/00bdd890.md)

## 疑似コード / UTF-8 4528 bytes

~~~c

byte * FUN_005abeac(long param_1,byte *param_2,byte *param_3,long param_4)

{
  byte bVar1;
  ulong uVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  int iVar7;
  
  if (param_2 == param_3) {
    return param_2;
  }
  bVar1 = *param_2;
  uVar2 = (ulong)bVar1;
  if (bVar1 < 0x72) {
    if (bVar1 < 0x66) {
      if (bVar1 == 0x30) {
        if (param_4 != 0) {
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0);
          goto LAB_005ac194;
        }
        uVar2 = 0;
      }
      else {
        if (bVar1 == 99) {
          if ((param_2 + 1 != param_3) && (bVar1 = param_2[1], (byte)((bVar1 & 0xdf) + 0xbf) < 0x1a)
             ) {
            if (param_4 != 0) {
              _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4);
              return param_2 + 2;
            }
            FUN_005ac1ac(param_1,bVar1 & 0x1f);
            return param_2 + 2;
          }
          goto LAB_005ac1a8;
        }
        if (bVar1 == 0x5f) goto LAB_005ac1a8;
LAB_005ac168:
        if ((-1 < (char)bVar1) &&
           ((*(ulong *)(*(long *)(*(long *)(param_1 + 8) + 0x10) + uVar2 * 8) & 0x60) != 0))
        goto LAB_005ac1a8;
        if (param_4 != 0) {
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4);
          goto LAB_005ac194;
        }
      }
    }
    else if (bVar1 == 0x66) {
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0xc);
        goto LAB_005ac194;
      }
      uVar2 = 0xc;
    }
    else {
      if (bVar1 != 0x6e) goto LAB_005ac168;
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,10);
        goto LAB_005ac194;
      }
      uVar2 = 10;
    }
  }
  else {
    if (0x74 < bVar1) {
      if (bVar1 == 0x75) {
        if (param_2 + 1 == param_3) goto LAB_005ac1a8;
        bVar1 = param_2[1];
        uVar4 = (uint)bVar1;
        iVar3 = 0xffd0;
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar4 = bVar1 | 0x20;
          if (5 < uVar4 - 0x61) goto LAB_005ac1a8;
          iVar3 = 0xffa9;
        }
        param_2 = param_2 + 2;
        if (param_2 == param_3) goto LAB_005ac1a8;
        bVar1 = *param_2;
        uVar6 = (uint)bVar1;
        iVar5 = 0xffd0;
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar6 = uVar6 | 0x20;
          if (5 < uVar6 - 0x61) goto LAB_005ac1a8;
          iVar5 = 0xffa9;
        }
        iVar3 = (iVar3 + uVar4) * 0x100 + (iVar5 + uVar6) * 0x10;
      }
      else {
        if (bVar1 == 0x76) {
          if (param_4 != 0) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0xb);
            goto LAB_005ac194;
          }
          uVar2 = 0xb;
          goto LAB_005ac190;
        }
        if (bVar1 != 0x78) goto LAB_005ac168;
        iVar3 = 0;
      }
      if (param_2 + 1 != param_3) {
        bVar1 = param_2[1];
        uVar4 = (uint)bVar1;
        iVar5 = 0xffd0;
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar4 = uVar4 | 0x20;
          if (5 < uVar4 - 0x61) goto LAB_005ac1a8;
          iVar5 = 0xffa9;
        }
        if (param_2 + 2 != param_3) {
          bVar1 = param_2[2];
          uVar6 = (uint)bVar1;
          iVar7 = 0xffd0;
          if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
            uVar6 = uVar6 | 0x20;
            if (5 < uVar6 - 0x61) goto LAB_005ac1a8;
            iVar7 = 0xffa9;
          }
          if (param_4 != 0) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4);
            return param_2 + 3;
          }
          FUN_005ac1ac(param_1,iVar7 + uVar6 + (iVar5 + uVar4 + iVar3) * 0x10);
          return param_2 + 3;
        }
      }
LAB_005ac1a8:
                    /* WARNING: Subroutine does not return */
      FUN_005abb94();
    }
    if (bVar1 == 0x72) {
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0xd);
        goto LAB_005ac194;
      }
      uVar2 = 0xd;
    }
    else {
      if (bVar1 != 0x74) goto LAB_005ac168;
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,9);
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
