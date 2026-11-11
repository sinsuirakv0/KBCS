# 009dfdac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009dfdac",
  "name": "FUN_009dfdac",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df6dc82b76bdef2cca79aa2572a4787c1d0144aae74bfc68abba5809326f2fc8",
  "source_text_sha256": "df6dc82b76bdef2cca79aa2572a4787c1d0144aae74bfc68abba5809326f2fc8"
}
~~~

## 呼び出し元

- [00ad0958](../00ad0/00ad0958.md)

## 呼び出し先

- [005c179c](../005c1/005c179c.md)
- [009dfb18](../009df/009dfb18.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 419 bytes

~~~c

bool FUN_009dfdac(void)

{
  long lVar1;
  undefined1 auStack_40 [8];
  undefined8 local_38;
  ulong uStack_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_009dfb18(auStack_40);
  FUN_005c179c(auStack_40,local_38);
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return 1 < uStack_30;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
