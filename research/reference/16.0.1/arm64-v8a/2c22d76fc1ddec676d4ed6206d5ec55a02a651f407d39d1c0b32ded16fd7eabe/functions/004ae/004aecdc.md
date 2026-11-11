# 004aecdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "004aecdc",
  "name": "_ZNK5Botan9X509_Time3cmpERKS0_",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00da6c14accec90e07925b05ed72148891b687f22b4f430d316c547a1780b287",
  "source_text_sha256": "00da6c14accec90e07925b05ed72148891b687f22b4f430d316c547a1780b287"
}
~~~

## 呼び出し元

- [00c589e0](../00c58/00c589e0.md)

## 呼び出し先

- [0043ddd8](../0043d/0043ddd8.md)
- [004aec64](../004ae/004aec64.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57ef0](../00c57/00c57ef0.md)
- [00c57f10](../00c57/00c57f10.md)

## 関連文字列（未確認候補）

~~~text
"X509_Time::cmp: No time set"
~~~

## 疑似コード / UTF-8 1814 bytes

~~~c

void _ZNK5Botan9X509_Time3cmpERKS0_(long param_1,long param_2)

{
  uint uVar1;
  long lVar2;
  ulong uVar3;
  undefined8 uVar4;
  undefined1 auStack_50 [24];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  uVar1 = *(uint *)(param_1 + 8);
  if (uVar1 == 0) {
    uVar4 = __cxa_allocate_exception(0x20);
    FUN_0043ddd8(auStack_50,"X509_Time::cmp: No time set");
    uVar3 = FUN_004aec64(uVar4,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar4,PTR__ZTIN5Botan13Invalid_StateE_00c9ad48,FUN_00535868);
    }
    goto LAB_004aee58;
  }
  if (uVar1 < *(uint *)(param_2 + 8)) {
LAB_004aed10:
    uVar3 = 0xffffffff;
  }
  else if (uVar1 == *(uint *)(param_2 + 8)) {
    if (*(uint *)(param_1 + 0xc) < *(uint *)(param_2 + 0xc)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0xc) < *(uint *)(param_1 + 0xc)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x10) < *(uint *)(param_2 + 0x10)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0x10) < *(uint *)(param_1 + 0x10)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x14) < *(uint *)(param_2 + 0x14)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0x14) < *(uint *)(param_1 + 0x14)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x18) < *(uint *)(param_2 + 0x18)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0x18) < *(uint *)(param_1 + 0x18)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x1c) < *(uint *)(param_2 + 0x1c)) goto LAB_004aed10;
    uVar3 = (ulong)(*(uint *)(param_2 + 0x1c) < *(uint *)(param_1 + 0x1c));
  }
  else {
LAB_004aed1c:
    uVar3 = 1;
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_004aee58:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar3);
}

~~~
