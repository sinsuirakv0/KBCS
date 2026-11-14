# 004beefc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004beefc",
  "name": "_ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e834c2464785b3f6cde02248ec5948b035ccd4f6f5b05d7ff91cc279f2f4e65",
  "source_text_sha256": "8e834c2464785b3f6cde02248ec5948b035ccd4f6f5b05d7ff91cc279f2f4e65"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459830](../00459/00459830.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59e40](../00c59/00c59e40.md)

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
  uVar3 = FUN_00459830(param_1,"CPUID flags: ",0xd);
  _ZN5Botan5CPUID9to_stringEv(&local_50);
  puVar2 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar2 = auStack_4f;
  }
  uVar3 = FUN_00459830(uVar3,puVar2,local_48);
  FUN_00459830(uVar3,&DAT_002b4cef,1);
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
