# 00ac7ffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00ac7ffc",
  "name": "FUN_00ac7ffc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f2e2d247eccab25239394b787321cdd2c74044a1c7a470b99565eb0fba1b0d5",
  "source_text_sha256": "3f2e2d247eccab25239394b787321cdd2c74044a1c7a470b99565eb0fba1b0d5"
}
~~~

## 呼び出し元

- [0098dc5c](../0098d/0098dc5c.md)

## 呼び出し先

- [00459db4](../00459/00459db4.md)

## 疑似コード / UTF-8 423 bytes

~~~c

bool FUN_00ac7ffc(long param_1)

{
  int iVar1;
  
  iVar1 = *(int *)(param_1 + 0xa4);
  *(int *)(param_1 + 0xa4) = iVar1 + 1;
  if (0x17 < iVar1) {
    if (*(long **)(param_1 + 0x160) == (long *)0x0) {
                    /* WARNING: Subroutine does not return */
      FUN_00459db4();
    }
    (**(code **)(**(long **)(param_1 + 0x160) + 0x30))();
    *(undefined1 *)(param_1 + 0xa0) = 0;
  }
  return 0x17 < iVar1;
}

~~~
