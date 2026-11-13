# 00acaaa8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acaaa8",
  "name": "FUN_00acaaa8",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae02632717f98fe77b5f90be10db20dcf17cec2d43cd6ef05ba1f4a9f5aa9d5d",
  "source_text_sha256": "ae02632717f98fe77b5f90be10db20dcf17cec2d43cd6ef05ba1f4a9f5aa9d5d"
}
~~~

## 呼び出し元

- [0082fbc4](../0082f/0082fbc4.md)
- [00997090](../00997/00997090.md)

## 呼び出し先

- [004678a0](../00467/004678a0.md)
- [00467b6c](../00467/00467b6c.md)
- [00467f94](../00467/00467f94.md)
- [0046ca04](../0046c/0046ca04.md)
- [0046cac4](../0046c/0046cac4.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 603 bytes

~~~c

void FUN_00acaaa8(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0xa0) != '\0') {
    uVar4 = FUN_004678a0();
    iVar1 = *(int *)(param_1 + 0xa4) * 0x14;
    if (0xfe < iVar1) {
      iVar1 = 0xff;
    }
    FUN_00467b6c(uVar4,0,0,0,iVar1);
    lVar5 = FUN_00851550();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_00851550();
    uVar2 = FUN_0046ca04();
    FUN_00851550();
    uVar3 = FUN_0046cac4();
    FUN_00467f94(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~
