# 006afcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `006afcec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcec.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "006afcec",
  "name": "FUN_006afcec",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "de98d859345bbf58a955d0b8cf882bf2205db4e7eb3a5c8defb302c42f90ac9e",
  "source_text_sha256": "de98d859345bbf58a955d0b8cf882bf2205db4e7eb3a5c8defb302c42f90ac9e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00666298](../00666/00666298.md)
- [006abb50](../006ab/006abb50.md)
- [0081f580](../0081f/0081f580.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 1537 bytes

~~~c

void FUN_006afcec(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  undefined8 uVar6;
  long lVar7;
  undefined8 local_48;
  long *local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar7 = *(long *)(param_1 + 8);
    FUN_006abb50(lVar7);
    lVar5 = FUN_0081f580();
    local_48 = *(undefined8 *)(lVar7 + 0x100);
    local_40 = *(long **)(lVar7 + 0x108);
    if (local_40 != (long *)0x0) {
      FUN_00bd6d60(1,local_40 + 1);
    }
    FUN_00666298(lVar5 + 0x16f0,&local_48);
    plVar3 = local_40;
    if ((local_40 != (long *)0x0) &&
       (lVar5 = FUN_00bd6d90(0xffffffffffffffff,local_40 + 1), lVar5 == 0)) {
      (**(code **)(*plVar3 + 0x10))(plVar3);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
    }
    lVar5 = FUN_0081f580();
    *(undefined4 *)(lVar5 + 0x472b28) = 1;
  }
  else {
    if (iVar1 == 3) {
      uVar4 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar6 = 0xb;
        goto LAB_006afd58;
      }
      goto LAB_006afe38;
    }
    if (iVar1 == 0) {
      uVar4 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_006afe38;
      uVar6 = 10;
LAB_006afd58:
      FUN_00459efc(uVar4,uVar6,0);
      return;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_006afe38:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
