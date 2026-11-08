# 00ba8fec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ba8fec",
  "name": "_ZNSt6__ndk114collate_bynameIwEC1EPKcm",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4664daa3dd4461f5bc41334ba1eb7974b36444685403ed7cf98959fc6b971f31",
  "source_text_sha256": "4664daa3dd4461f5bc41334ba1eb7974b36444685403ed7cf98959fc6b971f31"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0041b298](../0041b/0041b298.md)
- [00ba8a80](../00ba8/00ba8a80.md)
- [00bd70ac](../00bd7/00bd70ac.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb460](../00bdb/00bdb460.md)
- [00be0f60](../00be0/00be0f60.md)
- [00be1520](../00be1/00be1520.md)

## 関連文字列（未確認候補）

~~~text
"collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for "
~~~

## 疑似コード / UTF-8 1078 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIwEC1EPKcm(long *param_1,char *param_2,long param_3)

{
  undefined1 *puVar1;
  __locale_t p_Var2;
  undefined8 uVar3;
  byte local_50 [16];
  void *local_40;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk114collate_bynameIwEE_00c1bf40 + 0x10);
  param_1[1] = param_3 + -1;
  p_Var2 = newlocale(0x1fbf,param_2,(__locale_t)0x0);
  param_1[2] = (long)p_Var2;
  if (p_Var2 != (__locale_t)0x0) {
    return;
  }
  FUN_0041b298(local_50,param_2);
  FUN_00ba8a80(&local_38,
               "collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for ",
               local_50);
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar3 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
                    /* WARNING: Subroutine does not return */
  FUN_00bd70ac(uVar3);
}

~~~
