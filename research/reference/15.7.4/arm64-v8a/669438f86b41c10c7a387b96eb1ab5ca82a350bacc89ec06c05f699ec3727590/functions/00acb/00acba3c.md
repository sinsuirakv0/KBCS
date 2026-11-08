# 00acba3c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00acba3c",
  "name": "FUN_00acba3c",
  "size": 628,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ada82b445c61c9efe80fb990ca05310b08417c89e9553abb9ce3478562cf85fa",
  "source_text_sha256": "ada82b445c61c9efe80fb990ca05310b08417c89e9553abb9ce3478562cf85fa"
}
~~~

## 呼び出し元

- [004184bc](../00418/004184bc.md)

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041c9e0](../0041c/0041c9e0.md)
- [00449bb8](../00449/00449bb8.md)
- [00449be4](../00449/00449be4.md)
- [004723a8](../00472/004723a8.md)
- [0052e34c](../0052e/0052e34c.md)
- [00574768](../00574/00574768.md)
- [0081f580](../0081f/0081f580.md)
- [00828e20](../00828/00828e20.md)
- [00acd52c](../00acd/00acd52c.md)
- [00acd530](../00acd/00acd530.md)
- [00acd5b0](../00acd/00acd5b0.md)
- [00acd5b4](../00acd/00acd5b4.md)
- [00bd6558](../00bd6/00bd6558.md)
- [00bd65f8](../00bd6/00bd65f8.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb640](../00bdb/00bdb640.md)

## 疑似コード / UTF-8 3442 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acba3c(void)

{
  long lVar1;
  long *plVar2;
  int iVar3;
  ulong uVar4;
  long lVar5;
  undefined ***pppuVar6;
  long lVar7;
  float fVar8;
  undefined4 uVar9;
  undefined8 local_80;
  long *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_0081f580();
  uVar4 = FUN_00449be4();
  if ((uVar4 & 1) != 0) {
    if (*(long *)(lVar1 + 0x28) == local_38) {
      thunk_FUN_00569550();
      return;
    }
    goto LAB_00acbd10;
  }
  FUN_0081f580();
  uVar4 = FUN_00449bb8();
  if ((uVar4 & 1) != 0) {
    lVar5 = _ZNSt6__ndk16chrono12steady_clock3nowEv();
    FUN_0041be0c();
    FUN_0041c9e0();
    uVar4 = FUN_004723a8();
    if ((uVar4 & 1) != 0) {
      FUN_0081f580();
      iVar3 = FUN_00828e20();
      if (iVar3 != 0x65) {
        FUN_0081f580();
        iVar3 = FUN_00828e20();
        if (iVar3 != 0x67) {
          FUN_0081f580();
          iVar3 = FUN_00828e20();
          if (iVar3 != 0x61) {
            local_80 = 0;
            local_78 = (long *)0x0;
            local_70[0] = &PTR_FUN_00c0f748;
            local_50 = local_70;
            (**(code **)(**(long **)PTR_DAT_00c1b450 + 0xe8))
                      (*(long **)PTR_DAT_00c1b450,&local_80,local_70);
            if (local_50 == local_70) {
              lVar5 = 0x20;
              pppuVar6 = local_70;
LAB_00acbc70:
              (**(code **)((long)*pppuVar6 + lVar5))();
            }
            else if (local_50 != (undefined ***)0x0) {
              lVar5 = 0x28;
              pppuVar6 = local_50;
              goto LAB_00acbc70;
            }
            FUN_0052e34c(&local_80);
            goto LAB_00acbc84;
          }
        }
      }
    }
    local_80 = 0;
    local_78 = (long *)0x0;
    local_70[0] = &PTR_FUN_00c0f7c8;
    local_50 = local_70;
    (**(code **)(**(long **)PTR_DAT_00c1b450 + 0xe8))(*(long **)PTR_DAT_00c1b450,&local_80,local_70)
    ;
    if (local_50 == local_70) {
      lVar7 = 0x20;
      pppuVar6 = local_70;
LAB_00acbb40:
      (**(code **)((long)*pppuVar6 + lVar7))();
    }
    else if (local_50 != (undefined ***)0x0) {
      lVar7 = 0x28;
      pppuVar6 = local_50;
      goto LAB_00acbb40;
    }
    plVar2 = local_78;
    if ((local_78 != (long *)0x0) &&
       (lVar7 = FUN_00bd6e90(0xffffffffffffffff,local_78 + 1), lVar7 == 0)) {
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    lVar7 = _ZNSt6__ndk16chrono12steady_clock3nowEv();
    fVar8 = (float)(lVar7 - lVar5) / 1e+09;
    if ((fVar8 < 0.033333335) && (fVar8 = 0.033333335 - fVar8, 0.0 < fVar8)) {
      uVar9 = FUN_00bd65f8(fVar8);
      iVar3 = FUN_00bd6558(uVar9,_DAT_002b0de0);
      if (iVar3 < 0) {
        local_70[0] = (undefined **)(long)(fVar8 * 1e+09);
        if ((float)(long)local_70[0] < fVar8 * 1e+09) {
          local_70[0] = (undefined **)((long)local_70[0] + 1);
        }
      }
      else {
        local_70[0] = (undefined **)0x7fffffffffffffff;
      }
      _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE
                (local_70);
    }
  }
LAB_00acbc84:
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00acbd10:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
