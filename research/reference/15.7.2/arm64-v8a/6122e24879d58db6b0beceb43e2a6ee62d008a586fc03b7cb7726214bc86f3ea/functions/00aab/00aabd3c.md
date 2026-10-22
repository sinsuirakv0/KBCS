# 00aabd3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aabd3c.md)

## 関数情報

~~~json
{
  "address": "00aabd3c",
  "name": "FUN_00aabd3c",
  "size": 1164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "346490fc2b6a439fd796222e1ed3185f734135f343fab6c4f08b1a396a3dd0e6",
  "source_text_sha256": "346490fc2b6a439fd796222e1ed3185f734135f343fab6c4f08b1a396a3dd0e6"
}
~~~
## 呼び出し元

- [00aab67c](../00aab/00aab67c.md)
- [00aad8d8](../00aad/00aad8d8.md)
- [00aada14](../00aad/00aada14.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [004253b4](../00425/004253b4.md)
- [0045b734](../0045b/0045b734.md)
- [00469f7c](../00469/00469f7c.md)
- [0063fa4c](../0063f/0063fa4c.md)
- [0081f580](../0081f/0081f580.md)
- [00883d2c](../00883/00883d2c.md)
- [008847e4](../00884/008847e4.md)
- [00a25194](../00a25/00a25194.md)
- [00a25380](../00a25/00a25380.md)
- [00aab3c0](../00aab/00aab3c0.md)
- [00aab518](../00aab/00aab518.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"array::at"
"backstage_reset1"
"uni.imgcut"
~~~
## 疑似コード 1/1 / UTF-8 6417 bytes

~~~c

void FUN_00aabd3c(long param_1,long param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  int iVar5;
  long *plVar6;
  long lVar7;
  undefined8 uVar8;
  uint uVar9;
  ulong uVar10;
  long lVar11;
  __shared_weak_count *this;
  undefined8 *puVar12;
  long lVar13;
  __shared_weak_count *p_Var14;
  char *pcVar15;
  byte local_b0;
  undefined7 uStack_af;
  char cStack_a8;
  undefined7 uStack_a7;
  char local_a0;
  undefined1 uStack_9f;
  undefined6 uStack_9e;
  byte local_98 [11];
  undefined1 local_8d;
  void *local_88;
  ulong local_80;
  __shared_weak_count *p_Stack_78;
  void *local_70;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  *(undefined4 *)(param_1 + 0x48) = param_3;
  plVar6 = (long *)FUN_00aab518(param_1,param_3,0xffffffff,0,0);
  lVar7 = *plVar6;
  if (plVar6[1] == lVar7) {
    uVar10 = 0;
  }
  else {
    lVar11 = 0;
    puVar12 = (undefined8 *)(param_2 + 8);
    lVar13 = -10;
    do {
      FUN_0063fa4c(&local_80,*(undefined4 *)(lVar7 + lVar11),((undefined4 *)(lVar7 + lVar11))[1],0);
      p_Var14 = p_Stack_78;
      uVar10 = local_80;
      if (lVar13 == 0) {
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("array::at");
        }
        goto LAB_00aac28c;
      }
      this = (__shared_weak_count *)*puVar12;
      local_80 = 0;
      p_Stack_78 = (__shared_weak_count *)0x0;
      *puVar12 = p_Var14;
      puVar12[-1] = uVar10;
      p_Var14 = p_Stack_78;
      if ((this != (__shared_weak_count *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,this + 8), p_Var14 = p_Stack_78, lVar7 == 0)) {
        (**(code **)(*(long *)this + 0x10))(this);
        std::__ndk1::__shared_weak_count::__release_weak(this);
        p_Var14 = p_Stack_78;
      }
      p_Stack_78 = p_Var14;
      if ((p_Var14 != (__shared_weak_count *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,p_Var14 + 8), lVar7 == 0)) {
        (**(code **)(*(long *)p_Var14 + 0x10))(p_Var14);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var14);
      }
      lVar7 = *plVar6;
      uVar1 = lVar13 + 0xb;
      lVar13 = lVar13 + 1;
      puVar12 = puVar12 + 2;
      lVar11 = lVar11 + 8;
      uVar10 = plVar6[1] - lVar7 >> 3;
    } while (uVar1 < uVar10);
  }
  uVar8 = s_uni_imgcut_002a77c6._0_8_;
  uVar9 = (uint)uVar10;
  if ((int)uVar9 < 10) {
    if (uVar9 < 0xb) {
      uVar9 = 10;
    }
    pcVar15 = (char *)((ulong)local_98 | 1);
    lVar7 = -(uVar10 & 0xffffffff);
    puVar12 = (undefined8 *)(param_2 + (uVar10 & 0xffffffff) * 0x10 + 8);
    do {
      if (((DAT_00c24f78 & 1) == 0) && (iVar5 = __cxa_guard_acquire(&DAT_00c24f78), iVar5 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      p_Stack_78 = (__shared_weak_count *)((ulong)p_Stack_78 & 0xffffffffffffff00);
      local_80 = CONCAT71(local_80._1_7_,0xe);
      local_98[0] = 0x14;
      *(undefined4 *)((ulong)&local_80 | 1) = 0x2e696e75;
      *(undefined4 *)((long)((ulong)&local_80 | 1) + 3) = 0x676e702e;
      pcVar15[8] = 'u';
      pcVar15[9] = 't';
      *(undefined8 *)pcVar15 = uVar8;
      local_8d = 0;
      FUN_0045b734(&local_b0,&DAT_00c24f40,&local_80,local_98,0x2601);
      if (-(ulong)uVar9 == lVar7) {
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("array::at");
        }
        goto LAB_00aac28c;
      }
      uVar4 = CONCAT71(uStack_a7,cStack_a8);
      uVar3 = CONCAT71(uStack_af,local_b0);
      p_Var14 = (__shared_weak_count *)*puVar12;
      local_b0 = 0;
      uStack_af = 0;
      cStack_a8 = '\0';
      uStack_a7 = 0;
      *puVar12 = uVar4;
      puVar12[-1] = uVar3;
      if ((p_Var14 == (__shared_weak_count *)0x0) ||
         (lVar13 = FUN_00bd6d90(0xffffffffffffffff,p_Var14 + 8), lVar13 != 0)) {
        p_Var14 = (__shared_weak_count *)CONCAT71(uStack_a7,cStack_a8);
      }
      else {
        (**(code **)(*(long *)p_Var14 + 0x10))(p_Var14);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var14);
        p_Var14 = (__shared_weak_count *)CONCAT71(uStack_a7,cStack_a8);
      }
      if ((p_Var14 != (__shared_weak_count *)0x0) &&
         (lVar13 = FUN_00bd6d90(0xffffffffffffffff,p_Var14 + 8), lVar13 == 0)) {
        (**(code **)(*(long *)p_Var14 + 0x10))(p_Var14);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var14);
      }
      if ((local_98[0] & 1) != 0) {
        operator_delete(local_88);
      }
      if ((local_80 & 1) != 0) {
        operator_delete(local_70);
      }
      lVar7 = lVar7 + -1;
      puVar12 = puVar12 + 2;
    } while (lVar7 != -10);
  }
  lVar7 = FUN_0081f580();
  uVar8 = FUN_008847e4(lVar7 + 0x2e48,0x329);
  iVar5 = FUN_00aab3c0(param_1,0xffffffff,0,0);
  FUN_00883d2c(uVar8,1 < iVar5);
  lVar7 = FUN_0081f580();
  uVar8 = FUN_008847e4(lVar7 + 0x2e48,0x32a);
  iVar5 = FUN_00aab3c0(param_1,0xffffffff,0,0);
  FUN_00883d2c(uVar8,1 < iVar5);
  lVar7 = FUN_0081f580();
  FUN_00a25194(lVar7 + 0x2f88,0x66);
  lVar7 = FUN_0081f580();
  uStack_9f = 0;
  local_b0 = 0x20;
  uStack_a7 = (undefined7)s_backstage_reset1_002951bc._8_8_;
  local_a0 = SUB81(s_backstage_reset1_002951bc._8_8_,7);
  uStack_af = (undefined7)s_backstage_reset1_002951bc._0_8_;
  cStack_a8 = SUB81(s_backstage_reset1_002951bc._0_8_,7);
  FUN_00469f7c(local_98,&local_b0);
  FUN_004253b4(&local_80,local_98,0,*(int *)(param_1 + 0x48) + 1);
  FUN_00a25380(lVar7 + 0x2f88,0x66,&local_80,0x1e,0);
  if ((local_80 & 1) != 0) {
    operator_delete(local_70);
  }
  if ((local_98[0] & 1) != 0) {
    operator_delete(local_88);
  }
  if ((local_b0 & 1) != 0) {
    operator_delete((void *)CONCAT62(uStack_9e,CONCAT11(uStack_9f,local_a0)));
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
LAB_00aac28c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
