# 00aaeec0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aaeec0",
  "name": "FUN_00aaeec0",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d84d5260c3625f383cd0bf9e68ef8bc2f4aba9a6cf382e594f19625f0614dc56",
  "source_text_sha256": "d84d5260c3625f383cd0bf9e68ef8bc2f4aba9a6cf382e594f19625f0614dc56"
}
~~~

## 呼び出し元

- [009bd6b8](../009bd/009bd6b8.md)

## 呼び出し先

- [0045d420](../0045d/0045d420.md)
- [0045d518](../0045d/0045d518.md)

## 疑似コード / UTF-8 1132 bytes

~~~c

void FUN_00aaeec0(undefined4 *param_1,undefined8 param_2,uint param_3)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  
  uVar2 = FUN_0045d518(param_2);
  *param_1 = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[3] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[5] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[4] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[1] = uVar2;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)(param_1 + 7) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1d) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1e) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1f) = iVar3 != 0;
  uVar2 = FUN_0045d518(param_2);
  param_1[2] = uVar2;
  if (0x23 < (int)param_3) {
    iVar3 = FUN_0045d518(param_2);
    *(bool *)(param_1 + 8) = iVar3 != 0;
    if (0x9dc < param_3 >> 5) {
      iVar3 = FUN_0045d518(param_2);
      *(bool *)(param_1 + 9) = iVar3 != 0;
      if (0x18703 < param_3) {
        bVar1 = FUN_0045d420(param_2);
        *(byte *)(param_1 + 0xb) = bVar1 & 1;
      }
    }
  }
  return;
}

~~~
