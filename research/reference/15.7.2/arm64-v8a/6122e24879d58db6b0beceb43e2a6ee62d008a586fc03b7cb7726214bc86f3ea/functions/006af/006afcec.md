# 006afcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006afcec.md)

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
  "source_sha256": "b753e0fcf7e39fff66b567b39ac65c6eac152d49897b6160b682418e336b220d",
  "source_text_sha256": "b753e0fcf7e39fff66b567b39ac65c6eac152d49897b6160b682418e336b220d"
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

## 疑似コード 1/1 / UTF-8 1670 bytes

~~~c

void FUN_006afcec(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  __shared_weak_count *this;
  undefined8 uVar3;
  long lVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 local_48;
  __shared_weak_count *local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar6 = *(long *)(param_1 + 8);
    FUN_006abb50(lVar6);
    lVar4 = FUN_0081f580();
    local_48 = *(undefined8 *)(lVar6 + 0x100);
    local_40 = *(__shared_weak_count **)(lVar6 + 0x108);
    if (local_40 != (__shared_weak_count *)0x0) {
      FUN_00bd6d60(1,local_40 + 8);
    }
    FUN_00666298(lVar4 + 0x16f0,&local_48);
    this = local_40;
    if ((local_40 != (__shared_weak_count *)0x0) &&
       (lVar4 = FUN_00bd6d90(0xffffffffffffffff,local_40 + 8), lVar4 == 0)) {
      (**(code **)(*(long *)this + 0x10))(this);
      std::__ndk1::__shared_weak_count::__release_weak(this);
    }
    lVar4 = FUN_0081f580();
    *(undefined4 *)(lVar4 + 0x472b28) = 1;
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar5 = 0xb;
        goto LAB_006afd58;
      }
      goto LAB_006afe38;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_006afe38;
      uVar5 = 10;
LAB_006afd58:
      FUN_00459efc(uVar3,uVar5,0);
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
