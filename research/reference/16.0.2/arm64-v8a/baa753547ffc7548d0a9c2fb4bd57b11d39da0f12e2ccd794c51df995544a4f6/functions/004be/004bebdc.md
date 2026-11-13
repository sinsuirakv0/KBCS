# 004bebdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "004bebdc",
  "name": "_ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba4877c45772c22105358d174148cd98935cda87c0e0af005a8ebe75e854a0f6",
  "source_text_sha256": "ba4877c45772c22105358d174148cd98935cda87c0e0af005a8ebe75e854a0f6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459510](../00459/00459510.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58e70](../00c58/00c58e70.md)

## 関連文字列（未確認候補）

~~~text
"CPUID flags: "
~~~

## 疑似コード / UTF-8 828 bytes

~~~c

void _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE(undefined8 param_1)

{
  long lVar1;
  undefined1 *puVar2;
  undefined8 uVar3;
  byte local_50;
  undefined1 auStack_4f [7];
  ulong local_48;
  undefined1 *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar3 = FUN_00459510(param_1,"CPUID flags: ",0xd);
  _ZN5Botan5CPUID9to_stringEv(&local_50);
  puVar2 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar2 = auStack_4f;
  }
  uVar3 = FUN_00459510(uVar3,puVar2,local_48);
  FUN_00459510(uVar3,&DAT_002b4c11,1);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
