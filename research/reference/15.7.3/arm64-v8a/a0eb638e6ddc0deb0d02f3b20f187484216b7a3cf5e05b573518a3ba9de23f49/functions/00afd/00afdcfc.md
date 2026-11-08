# 00afdcfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afdcfc",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_PS0_",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d31e7d4f8658c83b2257e9a89b993289a09d79d3c4d76321beeaba11d1ce427b",
  "source_text_sha256": "d31e7d4f8658c83b2257e9a89b993289a09d79d3c4d76321beeaba11d1ce427b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00bdecd0](../00bde/00bdecd0.md)

## 疑似コード / UTF-8 1415 bytes

~~~c

void _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_
               (undefined8 param_1,undefined8 param_2,byte *param_3)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  byte local_58 [8];
  ulong local_50;
  void *local_48;
  char local_40;
  long local_38;
  
                    /* try { // try from 00afdcfc to 00bfdd07 has its CatchHandler @ 00afebe4 */
                    /* try { // try from 00afdd08 to 00bfdd1f has its CatchHandler @ 00afeb88 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00afdd20 to 00c00b67 has its CatchHandler @ 00af560c */
  _ZN8firebase4Path11GetRelativeERKS0_S2_(local_58);
  if (local_40 == '\0') {
    uVar4 = 0;
    goto LAB_00afdd8c;
  }
  if (local_58 == param_3) {
LAB_00afdd6c:
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
    local_40 = '\0';
  }
  else {
    uVar1 = (ulong)(local_58[0] >> 1);
    pvVar3 = (void *)((ulong)local_58 | 1);
    if ((local_58[0] & 1) != 0) {
      uVar1 = local_50;
      pvVar3 = local_48;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_3,pvVar3,uVar1);
    if (local_40 != '\0') goto LAB_00afdd6c;
  }
  uVar4 = 1;
LAB_00afdd8c:
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~
