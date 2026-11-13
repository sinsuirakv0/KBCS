# 00a2fedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00a2fedc",
  "name": "FUN_00a2fedc",
  "size": 664,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0393a0952242a791dad232b3511da998761d067aebbce1ce9a700ba571033048",
  "source_text_sha256": "0393a0952242a791dad232b3511da998761d067aebbce1ce9a700ba571033048"
}
~~~

## 呼び出し元

- [00b2c4ec](../00b2c/00b2c4ec.md)

## 呼び出し先

- [0048ce94](../0048c/0048ce94.md)
- [004939d8](../00493/004939d8.md)
- [0077c8a4](../0077c/0077c8a4.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58020](../00c58/00c58020.md)
- [00c58030](../00c58/00c58030.md)
- [00c580d0](../00c58/00c580d0.md)

## 関連文字列（未確認候補）

~~~text
"scheme_item_param_"
~~~

## 疑似コード / UTF-8 3585 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

uint FUN_00a2fedc(undefined8 *param_1,undefined8 param_2)

{
  void *__src;
  undefined4 uVar1;
  int iVar2;
  size_t __n;
  long lVar3;
  long *plVar4;
  bool bVar5;
  uint uVar6;
  ulong *puVar7;
  undefined8 uVar8;
  void *unaff_x22;
  long *plVar9;
  long *plVar10;
  byte local_d8 [16];
  void *local_c8;
  ulong local_c0;
  ulong uStack_b8;
  void *local_b0;
  byte local_a8 [16];
  void *local_98;
  undefined4 local_90;
  int local_88;
  void *local_80;
  void *pvStack_78;
  undefined8 local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  plVar9 = (long *)*param_1;
  if (plVar9 == param_1 + 1) {
    uVar6 = 0;
  }
  else {
    do {
      __src = (void *)plVar9[6];
      uVar1 = (undefined4)plVar9[4];
      iVar2 = (int)plVar9[5];
      local_80 = (void *)0x0;
      pvStack_78 = (void *)0x0;
      __n = plVar9[7] - (long)__src;
      local_70 = 0;
      local_90 = uVar1;
      local_88 = iVar2;
      if (__n == 0) {
        unaff_x22 = (void *)0x0;
        if (iVar2 != 0) goto LAB_00a2ff9c;
LAB_00a2ffb0:
        _ZNSt6__ndk19to_stringEi(local_d8,uVar1);
        puVar7 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                                    (local_d8,0,"scheme_item_param_");
        local_b0 = (void *)puVar7[2];
        uStack_b8 = puVar7[1];
        local_c0 = *puVar7;
        puVar7[1] = 0;
        puVar7[2] = 0;
        *puVar7 = 0;
        FUN_0048ce94(local_a8,&local_c0);
        uVar6 = FUN_004939d8(param_2,local_a8);
        if ((local_a8[0] & 1) != 0) {
          _ZdlPv(local_98);
        }
        if ((local_c0 & 1) != 0) {
          _ZdlPv(local_b0);
        }
        if ((local_d8[0] & 1) != 0) {
          _ZdlPv(local_c8);
        }
      }
      else {
        if (0x1555555555555555 < (ulong)(((long)__n >> 2) * -0x5555555555555555)) {
          if (*(long *)(lVar3 + 0x28) == local_68) {
            uVar8 = FUN_0077c8a4(&local_80);
            if ((local_a8[0] & 1) != 0) {
              _ZdlPv(local_98);
            }
            if ((local_c0 & 1) != 0) {
              _ZdlPv(local_b0);
            }
            if ((local_d8[0] & 1) != 0) {
              _ZdlPv(local_c8);
            }
            if (unaff_x22 != (void *)0x0) {
              _ZdlPv(unaff_x22);
            }
            if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00c53ffc(uVar8);
            }
          }
          goto LAB_00a301a4;
        }
        unaff_x22 = (void *)_Znwm(__n);
        local_80 = unaff_x22;
        pvStack_78 = unaff_x22;
        memcpy(unaff_x22,__src,__n);
        if (iVar2 == 0) goto LAB_00a2ffb0;
LAB_00a2ff9c:
        uVar6 = 0;
      }
      if (unaff_x22 != (void *)0x0) {
        _ZdlPv(unaff_x22);
      }
      if ((uVar6 & 1) != 0) {
        uVar6 = 1;
        break;
      }
      plVar4 = (long *)plVar9[1];
      plVar10 = plVar9;
      if ((long *)plVar9[1] == (long *)0x0) {
        do {
          plVar9 = (long *)plVar10[2];
          bVar5 = (long *)*plVar9 != plVar10;
          plVar10 = plVar9;
        } while (bVar5);
      }
      else {
        do {
          plVar9 = plVar4;
          plVar4 = (long *)*plVar9;
        } while ((long *)*plVar9 != (long *)0x0);
      }
    } while (plVar9 != param_1 + 1);
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return uVar6 & 1;
  }
LAB_00a301a4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
