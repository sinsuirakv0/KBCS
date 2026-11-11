# 00bfacb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfacb4",
  "name": "_ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36b58cce38a11c2386bd499de5f82c52de0ab6a0f5711b84de4cdde2d82d0a41",
  "source_text_sha256": "36b58cce38a11c2386bd499de5f82c52de0ab6a0f5711b84de4cdde2d82d0a41"
}
~~~

## 呼び出し元

- [00c583a0](../00c58/00c583a0.md)

## 呼び出し先

- [00c580b0](../00c58/00c580b0.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5d610](../00c5d/00c5d610.md)

## 関連文字列（未確認候補）

~~~text
"random_device failed to open "
~~~

## 疑似コード / UTF-8 877 bytes

~~~c

void _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (int *param_1,byte *param_2)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 *puVar3;
  byte *__file;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  __file = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __file = param_2 + 1;
  }
  iVar2 = open((char *)__file,0);
  *param_1 = iVar2;
  if (-1 < iVar2) {
    return;
  }
  puVar3 = (undefined4 *)__errno();
  uVar1 = *puVar3;
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"random_device failed to open ",param_2);
  if ((local_38 & 1) == 0) {
    local_28 = auStack_37;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(uVar1,local_28);
}

~~~
