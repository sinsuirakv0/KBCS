# 00b5deec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b5deec",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_PS0_",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9bfd83e72f7c2defd46b4702b7e7b3ad1c4e32d36160edcdc54aaeddb952065",
  "source_text_sha256": "e9bfd83e72f7c2defd46b4702b7e7b3ad1c4e32d36160edcdc54aaeddb952065"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5bbe0](../00c5b/00c5bbe0.md)

## 疑似コード / UTF-8 1124 bytes

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
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  _ZN8firebase4Path11GetRelativeERKS0_S2_(local_58);
  if (local_40 == '\0') {
    uVar4 = 0;
    goto LAB_00b5df7c;
  }
  if (local_58 == param_3) {
LAB_00b5df5c:
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
    if (local_40 != '\0') goto LAB_00b5df5c;
  }
  uVar4 = 1;
LAB_00b5df7c:
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~
