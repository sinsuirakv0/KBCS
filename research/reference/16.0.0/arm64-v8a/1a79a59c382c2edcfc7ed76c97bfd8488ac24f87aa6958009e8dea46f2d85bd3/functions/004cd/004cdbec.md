# 004cdbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004aad54`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0009.md#compare-d4e0acb021125d51e01a38315dbf49d7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004cdc2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cdc2c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0009.md#compare-460e056efa79db2aa0ee6a40f3c55bac)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cdbec",
  "name": "_ZN5Botan7KeyPair28encryption_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringIcNS9_11char_traitsIcEENS9_9allocatorIcEEEE",
  "size": 832,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a08fedd2f8fb33c6e07496b25ccd1ba05bdb04e5d147e426f9208258ea325a8",
  "source_text_sha256": "9a08fedd2f8fb33c6e07496b25ccd1ba05bdb04e5d147e426f9208258ea325a8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cdbec",
        "004cdf27"
      ],
      [
        "004cdfdc",
        "004cdfdf"
      ]
    ],
    "bytes_sha256": "59b75c4279527f0b973756d4885af87320d84f648bec3f58cabb3c4983c8092e",
    "instruction_count": 208,
    "instruction_bytes": 832,
    "body_bytes": 832,
    "indirect": 6,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0049f3ec](../0049f/0049f3ec.md)
- [004b34c8](../004b3/004b34c8.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57b40](../00c57/00c57b40.md)
- [00c57c50](../00c57/00c57c50.md)
- [00c57c90](../00c57/00c57c90.md)
- [00c58260](../00c58/00c58260.md)
- [00c58dd0](../00c58/00c58dd0.md)
- [00c58de0](../00c58/00c58de0.md)
- [00c58df0](../00c58/00c58df0.md)
- [00c58e00](../00c58/00c58e00.md)
- [00c58e10](../00c58/00c58e10.md)
- [0112a058](../0112a/0112a058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4514 bytes

~~~c

bool _ZN5Botan7KeyPair28encryption_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringIcNS9_11char_traitsIcEENS9_9allocatorIcEEEE
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)

{
  long lVar1;
  void *pvVar2;
  bool bVar3;
  int iVar4;
  ulong uVar5;
  void *__s;
  void *pvVar6;
  size_t sVar7;
  size_t sVar8;
  long lVar9;
  void *local_e8;
  void *local_e0;
  long local_d8;
  void *local_d0;
  long local_c8;
  long local_c0;
  void *local_b8;
  void *local_b0;
  long local_a8;
  undefined1 auStack_a0 [16];
  void *local_90;
  void *local_88;
  void *local_80;
  long local_78;
  long *local_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  local_90 = (void *)((ulong)local_90 & 0xffffffffffff0000);
  _ZN5Botan16PK_Encryptor_EMEC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESE_
            (&local_78,param_3,param_1,param_4,&local_90);
  if (((ulong)local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  local_90 = (void *)((ulong)local_90 & 0xffffffffffff0000);
  _ZN5Botan16PK_Decryptor_EMEC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESE_
            (auStack_a0,param_2,param_1,param_4,&local_90);
  if (((ulong)local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  uVar5 = (**(code **)(*local_70 + 8))();
  if (uVar5 < 8) {
    bVar3 = true;
  }
  else {
    uVar5 = (**(code **)(*local_70 + 8))();
    FUN_004b34c8(&local_b8,(uVar5 >> 3) - 1);
    (**(code **)(*param_1 + 0x10))(param_1,local_b8,(long)local_b0 - (long)local_b8);
    pvVar2 = local_b8;
    local_88 = (void *)0x0;
    local_80 = (void *)0x0;
    local_90 = (void *)0x0;
    sVar7 = (long)local_b0 - (long)local_b8;
    if (sVar7 == 0) {
      pvVar6 = (void *)0x0;
      __s = (void *)0x0;
      pvVar2 = local_b0;
    }
    else {
      if ((long)sVar7 < 0) {
        if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0049f3ec(&local_90);
        }
        goto LAB_004cdfdc;
      }
      __s = (void *)_Znwm(sVar7);
      pvVar6 = (void *)((long)__s + sVar7);
      local_90 = __s;
      local_80 = pvVar6;
      memset(__s,0,sVar7);
      local_88 = pvVar6;
      memmove(__s,pvVar2,sVar7);
      pvVar2 = local_b8;
    }
    if (pvVar2 != (void *)0x0) {
      local_b0 = pvVar2;
      (*(code *)PTR_memset_00c67338)(pvVar2,0,local_a8 - (long)pvVar2);
      free(pvVar2);
    }
    sVar7 = (long)pvVar6 - (long)__s;
    (**(code **)(local_78 + 0x18))(&local_b8,&local_78,__s,sVar7,param_1);
    pvVar2 = local_b8;
    sVar8 = (long)local_b0 - (long)local_b8;
    if ((sVar8 == sVar7) && (iVar4 = memcmp(local_b8,__s,sVar7), iVar4 == 0)) {
      bVar3 = false;
      local_b8 = pvVar2;
    }
    else {
      _ZNK5Botan12PK_Decryptor7decryptEPKhm(&local_e8,auStack_a0,pvVar2,sVar8);
      pvVar2 = local_e8;
      local_c8 = 0;
      local_c0 = 0;
      local_d0 = (void *)0x0;
      sVar8 = (long)local_e0 - (long)local_e8;
      if (sVar8 == 0) {
        pvVar6 = (void *)0x0;
        lVar9 = 0;
      }
      else {
        if ((long)sVar8 < 0) {
          if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_0049f3ec(&local_d0);
          }
          goto LAB_004cdfdc;
        }
        pvVar6 = (void *)_Znwm(sVar8);
        lVar9 = (long)pvVar6 + sVar8;
        local_d0 = pvVar6;
        local_c0 = lVar9;
        memset(pvVar6,0,sVar8);
        local_c8 = lVar9;
        memmove(pvVar6,pvVar2,sVar8);
        local_e0 = local_e8;
      }
      if (local_e0 != (void *)0x0) {
        (*(code *)PTR_memset_00c67338)(local_e0,0,local_d8 - (long)local_e0);
        free(local_e0);
      }
      if (sVar7 == lVar9 - (long)pvVar6) {
        iVar4 = memcmp(__s,pvVar6,sVar7);
        bVar3 = iVar4 == 0;
      }
      else {
        bVar3 = false;
      }
      if (pvVar6 != (void *)0x0) {
        _ZdlPv(pvVar6);
      }
    }
    if (local_b8 != (void *)0x0) {
      _ZdlPv(local_b8);
    }
    if (__s != (void *)0x0) {
      _ZdlPv(__s);
    }
  }
  _ZN5Botan16PK_Decryptor_EMED1Ev(auStack_a0);
  _ZN5Botan16PK_Encryptor_EMED1Ev(&local_78);
  if (*(long *)(lVar1 + 0x28) == local_68) {
    return bVar3;
  }
LAB_004cdfdc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004cdbec"></a> `004cdbec` | `ff c3 03 d1` | sub sp,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-004cdbf0"></a> `004cdbf0` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004cdbf4"></a> `004cdbf4` | `fb 53 00 f9` | str x27,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004cdbf8"></a> `004cdbf8` | `fa 67 0b a9` | stp x26,x25,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004cdbfc"></a> `004cdbfc` | `f8 5f 0c a9` | stp x24,x23,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004cdc00"></a> `004cdc00` | `f6 57 0d a9` | stp x22,x21,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004cdc04"></a> `004cdc04` | `f4 4f 0e a9` | stp x20,x19,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-004cdc08"></a> `004cdc08` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-004cdc0c"></a> `004cdc0c` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004cdc10"></a> `004cdc10` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-004cdc14"></a> `004cdc14` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-004cdc18"></a> `004cdc18` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cdc1c"></a> `004cdc1c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004cdc20"></a> `004cdc20` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cdc24"></a> `004cdc24` | `bf 03 1d 78` | sturh wzr,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004cdc28"></a> `004cdc28` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-004cdc2c"></a> `004cdc2c` | `a4 c3 00 d1` | sub x4,x29,#0x30 | `FALL_THROUGH`
<a id="insn-004cdc30"></a> `004cdc30` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-004cdc34"></a> `004cdc34` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-004cdc38"></a> `004cdc38` | `66 2c 1e 94` | bl 0x00c58dd0 | `UNCONDITIONAL_CALL`
<a id="insn-004cdc3c"></a> `004cdc3c` | `a8 03 5d 38` | ldurb w8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004cdc40"></a> `004cdc40` | `68 00 00 36` | tbz w8,#0x0,0x004cdc4c | `CONDITIONAL_JUMP`
<a id="insn-004cdc44"></a> `004cdc44` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004cdc48"></a> `004cdc48` | `9a 27 1e 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004cdc4c"></a> `004cdc4c` | `bf 03 1d 78` | sturh wzr,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004cdc50"></a> `004cdc50` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-004cdc54"></a> `004cdc54` | `a4 c3 00 d1` | sub x4,x29,#0x30 | `FALL_THROUGH`
<a id="insn-004cdc58"></a> `004cdc58` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004cdc5c"></a> `004cdc5c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-004cdc60"></a> `004cdc60` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-004cdc64"></a> `004cdc64` | `5f 2c 1e 94` | bl 0x00c58de0 | `UNCONDITIONAL_CALL`
<a id="insn-004cdc68"></a> `004cdc68` | `a8 03 5d 38` | ldurb w8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004cdc6c"></a> `004cdc6c` | `68 00 00 36` | tbz w8,#0x0,0x004cdc78 | `CONDITIONAL_JUMP`
<a id="insn-004cdc70"></a> `004cdc70` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004cdc74"></a> `004cdc74` | `8f 27 1e 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004cdc78"></a> `004cdc78` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004cdc7c"></a> `004cdc7c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cdc80"></a> `004cdc80` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004cdc84"></a> `004cdc84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cdc88"></a> `004cdc88` | `1f 20 00 f1` | cmp x0,#0x8 | `FALL_THROUGH`
<a id="insn-004cdc8c"></a> `004cdc8c` | `62 00 00 54` | b.cs 0x004cdc98 | `CONDITIONAL_JUMP`
<a id="insn-004cdc90"></a> `004cdc90` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004cdc94"></a> `004cdc94` | `85 00 00 14` | b 0x004cdea8 | `UNCONDITIONAL_JUMP`
<a id="insn-004cdc98"></a> `004cdc98` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004cdc9c"></a> `004cdc9c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cdca0"></a> `004cdca0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004cdca4"></a> `004cdca4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cdca8"></a> `004cdca8` | `08 fc 43 d3` | lsr x8,x0,#0x3 | `FALL_THROUGH`
<a id="insn-004cdcac"></a> `004cdcac` | `01 05 00 d1` | sub x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004cdcb0"></a> `004cdcb0` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004cdcb4"></a> `004cdcb4` | `05 96 ff 97` | bl 0x004b34c8 | `UNCONDITIONAL_CALL`
<a id="insn-004cdcb8"></a> `004cdcb8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004cdcbc"></a> `004cdcbc` | `e1 a7 43 a9` | ldp x1,x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004cdcc0"></a> `004cdcc0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-004cdcc4"></a> `004cdcc4` | `22 01 01 cb` | sub x2,x9,x1 | `FALL_THROUGH`
<a id="insn-004cdcc8"></a> `004cdcc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cdccc"></a> `004cdccc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cdcd0"></a> `004cdcd0` | `f6 d7 43 a9` | ldp x22,x21,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004cdcd4"></a> `004cdcd4` | `bf ff 3d a9` | stp xzr,xzr,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004cdcd8"></a> `004cdcd8` | `bf 03 1d f8` | stur xzr,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004cdcdc"></a> `004cdcdc` | `b7 02 16 eb` | subs x23,x21,x22 | `FALL_THROUGH`
<a id="insn-004cdce0"></a> `004cdce0` | `80 02 00 54` | b.eq 0x004cdd30 | `CONDITIONAL_JUMP`
<a id="insn-004cdce4"></a> `004cdce4` | `b7 10 f8 b7` | tbnz x23,#0x3f,0x004cdef8 | `CONDITIONAL_JUMP`
<a id="insn-004cdce8"></a> `004cdce8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004cdcec"></a> `004cdcec` | `69 27 1e 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-004cdcf0"></a> `004cdcf0` | `18 00 17 8b` | add x24,x0,x23 | `FALL_THROUGH`
<a id="insn-004cdcf4"></a> `004cdcf4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004cdcf8"></a> `004cdcf8` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-004cdcfc"></a> `004cdcfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cdd00"></a> `004cdd00` | `a0 03 1d f8` | stur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004cdd04"></a> `004cdd04` | `b8 03 1e f8` | stur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004cdd08"></a> `004cdd08` | `e2 27 1e 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-004cdd0c"></a> `004cdd0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cdd10"></a> `004cdd10` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004cdd14"></a> `004cdd14` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-004cdd18"></a> `004cdd18` | `b8 83 1d f8` | stur x24,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004cdd1c"></a> `004cdd1c` | `89 27 1e 94` | bl 0x00c57b40 | `UNCONDITIONAL_CALL`
<a id="insn-004cdd20"></a> `004cdd20` | `f5 1f 40 f9` | ldr x21,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004cdd24"></a> `004cdd24` | `da 3c 00 d0` | adrp x26,0xc67000 | `FALL_THROUGH`
<a id="insn-004cdd28"></a> `004cdd28` | `d5 00 00 b5` | cbnz x21,0x004cdd40 | `CONDITIONAL_JUMP`
<a id="insn-004cdd2c"></a> `004cdd2c` | `0e 00 00 14` | b 0x004cdd64 | `UNCONDITIONAL_JUMP`
<a id="insn-004cdd30"></a> `004cdd30` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-004cdd34"></a> `004cdd34` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-004cdd38"></a> `004cdd38` | `da 3c 00 d0` | adrp x26,0xc67000 | `FALL_THROUGH`
<a id="insn-004cdd3c"></a> `004cdd3c` | `55 01 00 b4` | cbz x21,0x004cdd64 | `CONDITIONAL_JUMP`
<a id="insn-004cdd40"></a> `004cdd40` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cdd44"></a> `004cdd44` | `e8 27 40 f9` | ldr x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004cdd48"></a> `004cdd48` | `49 9f 41 f9` | ldr x9,[x26, #0x338] | `FALL_THROUGH`
<a id="insn-004cdd4c"></a> `004cdd4c` | `02 01 15 cb` | sub x2,x8,x21 | `FALL_THROUGH`
<a id="insn-004cdd50"></a> `004cdd50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004cdd54"></a> `004cdd54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004cdd58"></a> `004cdd58` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004cdd5c"></a> `004cdd5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004cdd60"></a> `004cdd60` | `40 29 1e 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004cdd64"></a> `004cdd64` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004cdd68"></a> `004cdd68` | `15 03 13 cb` | sub x21,x24,x19 | `FALL_THROUGH`
<a id="insn-004cdd6c"></a> `004cdd6c` | `09 0d 40 f9` | ldr x9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004cdd70"></a> `004cdd70` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004cdd74"></a> `004cdd74` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-004cdd78"></a> `004cdd78` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004cdd7c"></a> `004cdd7c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004cdd80"></a> `004cdd80` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-004cdd84"></a> `004cdd84` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004cdd88"></a> `004cdd88` | `f4 a3 43 a9` | ldp x20,x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004cdd8c"></a> `004cdd8c` | `16 01 14 cb` | sub x22,x8,x20 | `FALL_THROUGH`
<a id="insn-004cdd90"></a> `004cdd90` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-004cdd94"></a> `004cdd94` | `c1 00 00 54` | b.ne 0x004cddac | `CONDITIONAL_JUMP`
<a id="insn-004cdd98"></a> `004cdd98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cdd9c"></a> `004cdd9c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004cdda0"></a> `004cdda0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004cdda4"></a> `004cdda4` | `ab 27 1e 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-004cdda8"></a> `004cdda8` | `20 0a 00 34` | cbz w0,0x004cdeec | `CONDITIONAL_JUMP`
<a id="insn-004cddac"></a> `004cddac` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004cddb0"></a> `004cddb0` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-004cddb4"></a> `004cddb4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004cddb8"></a> `004cddb8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-004cddbc"></a> `004cddbc` | `0d 2c 1e 94` | bl 0x00c58df0 | `UNCONDITIONAL_CALL`
<a id="insn-004cddc0"></a> `004cddc0` | `f7 db 40 a9` | ldp x23,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cddc4"></a> `004cddc4` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004cddc8"></a> `004cddc8` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cddcc"></a> `004cddcc` | `d8 02 17 eb` | subs x24,x22,x23 | `FALL_THROUGH`
<a id="insn-004cddd0"></a> `004cddd0` | `60 02 00 54` | b.eq 0x004cde1c | `CONDITIONAL_JUMP`
<a id="insn-004cddd4"></a> `004cddd4` | `f8 09 f8 b7` | tbnz x24,#0x3f,0x004cdf10 | `CONDITIONAL_JUMP`
<a id="insn-004cddd8"></a> `004cddd8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004cdddc"></a> `004cdddc` | `2d 27 1e 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-004cdde0"></a> `004cdde0` | `1b 00 18 8b` | add x27,x0,x24 | `FALL_THROUGH`
<a id="insn-004cdde4"></a> `004cdde4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004cdde8"></a> `004cdde8` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-004cddec"></a> `004cddec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004cddf0"></a> `004cddf0` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cddf4"></a> `004cddf4` | `fb 1b 00 f9` | str x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cddf8"></a> `004cddf8` | `a6 27 1e 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-004cddfc"></a> `004cddfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cde00"></a> `004cde00` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004cde04"></a> `004cde04` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-004cde08"></a> `004cde08` | `fb 17 00 f9` | str x27,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004cde0c"></a> `004cde0c` | `4d 27 1e 94` | bl 0x00c57b40 | `UNCONDITIONAL_CALL`
<a id="insn-004cde10"></a> `004cde10` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cde14"></a> `004cde14` | `b6 00 00 b5` | cbnz x22,0x004cde28 | `CONDITIONAL_JUMP`
<a id="insn-004cde18"></a> `004cde18` | `0d 00 00 14` | b 0x004cde4c | `UNCONDITIONAL_JUMP`
<a id="insn-004cde1c"></a> `004cde1c` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-004cde20"></a> `004cde20` | `fb 03 1f aa` | mov x27,xzr | `FALL_THROUGH`
<a id="insn-004cde24"></a> `004cde24` | `56 01 00 b4` | cbz x22,0x004cde4c | `CONDITIONAL_JUMP`
<a id="insn-004cde28"></a> `004cde28` | `f6 0b 00 f9` | str x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cde2c"></a> `004cde2c` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004cde30"></a> `004cde30` | `49 9f 41 f9` | ldr x9,[x26, #0x338] | `FALL_THROUGH`
<a id="insn-004cde34"></a> `004cde34` | `02 01 16 cb` | sub x2,x8,x22 | `FALL_THROUGH`
<a id="insn-004cde38"></a> `004cde38` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004cde3c"></a> `004cde3c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004cde40"></a> `004cde40` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004cde44"></a> `004cde44` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004cde48"></a> `004cde48` | `06 29 1e 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004cde4c"></a> `004cde4c` | `68 03 14 cb` | sub x8,x27,x20 | `FALL_THROUGH`
<a id="insn-004cde50"></a> `004cde50` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-004cde54"></a> `004cde54` | `21 01 00 54` | b.ne 0x004cde78 | `CONDITIONAL_JUMP`
<a id="insn-004cde58"></a> `004cde58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cde5c"></a> `004cde5c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004cde60"></a> `004cde60` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004cde64"></a> `004cde64` | `7b 27 1e 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-004cde68"></a> `004cde68` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-004cde6c"></a> `004cde6c` | `f5 17 9f 1a` | cset w21,eq | `FALL_THROUGH`
<a id="insn-004cde70"></a> `004cde70` | `94 00 00 b5` | cbnz x20,0x004cde80 | `CONDITIONAL_JUMP`
<a id="insn-004cde74"></a> `004cde74` | `05 00 00 14` | b 0x004cde88 | `UNCONDITIONAL_JUMP`
<a id="insn-004cde78"></a> `004cde78` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004cde7c"></a> `004cde7c` | `74 00 00 b4` | cbz x20,0x004cde88 | `CONDITIONAL_JUMP`
<a id="insn-004cde80"></a> `004cde80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cde84"></a> `004cde84` | `0b 27 1e 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004cde88"></a> `004cde88` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004cde8c"></a> `004cde8c` | `94 00 00 b4` | cbz x20,0x004cde9c | `CONDITIONAL_JUMP`
<a id="insn-004cde90"></a> `004cde90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cde94"></a> `004cde94` | `f4 23 00 f9` | str x20,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cde98"></a> `004cde98` | `06 27 1e 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004cde9c"></a> `004cde9c` | `73 00 00 b4` | cbz x19,0x004cdea8 | `CONDITIONAL_JUMP`
<a id="insn-004cdea0"></a> `004cdea0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cdea4"></a> `004cdea4` | `03 27 1e 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004cdea8"></a> `004cdea8` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-004cdeac"></a> `004cdeac` | `d5 2b 1e 94` | bl 0x00c58e00 | `UNCONDITIONAL_CALL`
<a id="insn-004cdeb0"></a> `004cdeb0` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-004cdeb4"></a> `004cdeb4` | `d7 2b 1e 94` | bl 0x00c58e10 | `UNCONDITIONAL_CALL`
<a id="insn-004cdeb8"></a> `004cdeb8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cdebc"></a> `004cdebc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cdec0"></a> `004cdec0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cdec4"></a> `004cdec4` | `c1 08 00 54` | b.ne 0x004cdfdc | `CONDITIONAL_JUMP`
<a id="insn-004cdec8"></a> `004cdec8` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-004cdecc"></a> `004cdecc` | `f4 4f 4e a9` | ldp x20,x19,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-004cded0"></a> `004cded0` | `fb 53 40 f9` | ldr x27,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004cded4"></a> `004cded4` | `f6 57 4d a9` | ldp x22,x21,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004cded8"></a> `004cded8` | `f8 5f 4c a9` | ldp x24,x23,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004cdedc"></a> `004cdedc` | `fa 67 4b a9` | ldp x26,x25,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004cdee0"></a> `004cdee0` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004cdee4"></a> `004cdee4` | `ff c3 03 91` | add sp,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-004cdee8"></a> `004cdee8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cdeec"></a> `004cdeec` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004cdef0"></a> `004cdef0` | `14 fd ff b5` | cbnz x20,0x004cde90 | `CONDITIONAL_JUMP`
<a id="insn-004cdef4"></a> `004cdef4` | `ea ff ff 17` | b 0x004cde9c | `UNCONDITIONAL_JUMP`
<a id="insn-004cdef8"></a> `004cdef8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cdefc"></a> `004cdefc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cdf00"></a> `004cdf00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cdf04"></a> `004cdf04` | `c1 06 00 54` | b.ne 0x004cdfdc | `CONDITIONAL_JUMP`
<a id="insn-004cdf08"></a> `004cdf08` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-004cdf0c"></a> `004cdf0c` | `38 45 ff 97` | bl 0x0049f3ec | `CALL_TERMINATOR`
<a id="insn-004cdf10"></a> `004cdf10` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cdf14"></a> `004cdf14` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cdf18"></a> `004cdf18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cdf1c"></a> `004cdf1c` | `01 06 00 54` | b.ne 0x004cdfdc | `CONDITIONAL_JUMP`
<a id="insn-004cdf20"></a> `004cdf20` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004cdf24"></a> `004cdf24` | `32 45 ff 97` | bl 0x0049f3ec | `CALL_TERMINATOR`
<a id="insn-004cdfdc"></a> `004cdfdc` | `c1 26 1e 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cdbec`](#insn-004cdbec) 範囲 `[['004cdbec', '004cdc43']]`
  - `CONDITIONAL_JUMP` [`004cdc40`](#insn-004cdc40) → [`004cdc4c`](#insn-004cdc4c)
  - `FALL_THROUGH` [`004cdc40`](#insn-004cdc40) → [`004cdc44`](#insn-004cdc44)
- ブロック [`004cdc44`](#insn-004cdc44) 範囲 `[['004cdc44', '004cdc4b']]`
  - `FALL_THROUGH` [`004cdc48`](#insn-004cdc48) → [`004cdc4c`](#insn-004cdc4c)
- ブロック [`004cdc4c`](#insn-004cdc4c) 範囲 `[['004cdc4c', '004cdc6f']]`
  - `CONDITIONAL_JUMP` [`004cdc6c`](#insn-004cdc6c) → [`004cdc78`](#insn-004cdc78)
  - `FALL_THROUGH` [`004cdc6c`](#insn-004cdc6c) → [`004cdc70`](#insn-004cdc70)
- ブロック [`004cdc70`](#insn-004cdc70) 範囲 `[['004cdc70', '004cdc77']]`
  - `FALL_THROUGH` [`004cdc74`](#insn-004cdc74) → [`004cdc78`](#insn-004cdc78)
- ブロック [`004cdc78`](#insn-004cdc78) 範囲 `[['004cdc78', '004cdc8f']]`
  - `CONDITIONAL_JUMP` [`004cdc8c`](#insn-004cdc8c) → [`004cdc98`](#insn-004cdc98)
  - `FALL_THROUGH` [`004cdc8c`](#insn-004cdc8c) → [`004cdc90`](#insn-004cdc90)
- ブロック [`004cdc90`](#insn-004cdc90) 範囲 `[['004cdc90', '004cdc97']]`
  - `UNCONDITIONAL_JUMP` [`004cdc94`](#insn-004cdc94) → [`004cdea8`](#insn-004cdea8)
- ブロック [`004cdc98`](#insn-004cdc98) 範囲 `[['004cdc98', '004cdce3']]`
  - `CONDITIONAL_JUMP` [`004cdce0`](#insn-004cdce0) → [`004cdd30`](#insn-004cdd30)
  - `FALL_THROUGH` [`004cdce0`](#insn-004cdce0) → [`004cdce4`](#insn-004cdce4)
- ブロック [`004cdce4`](#insn-004cdce4) 範囲 `[['004cdce4', '004cdce7']]`
  - `CONDITIONAL_JUMP` [`004cdce4`](#insn-004cdce4) → [`004cdef8`](#insn-004cdef8)
  - `FALL_THROUGH` [`004cdce4`](#insn-004cdce4) → [`004cdce8`](#insn-004cdce8)
- ブロック [`004cdce8`](#insn-004cdce8) 範囲 `[['004cdce8', '004cdd2b']]`
  - `CONDITIONAL_JUMP` [`004cdd28`](#insn-004cdd28) → [`004cdd40`](#insn-004cdd40)
  - `FALL_THROUGH` [`004cdd28`](#insn-004cdd28) → [`004cdd2c`](#insn-004cdd2c)
- ブロック [`004cdd2c`](#insn-004cdd2c) 範囲 `[['004cdd2c', '004cdd2f']]`
  - `UNCONDITIONAL_JUMP` [`004cdd2c`](#insn-004cdd2c) → [`004cdd64`](#insn-004cdd64)
- ブロック [`004cdd30`](#insn-004cdd30) 範囲 `[['004cdd30', '004cdd3f']]`
  - `CONDITIONAL_JUMP` [`004cdd3c`](#insn-004cdd3c) → [`004cdd64`](#insn-004cdd64)
  - `FALL_THROUGH` [`004cdd3c`](#insn-004cdd3c) → [`004cdd40`](#insn-004cdd40)
- ブロック [`004cdd40`](#insn-004cdd40) 範囲 `[['004cdd40', '004cdd63']]`
  - `FALL_THROUGH` [`004cdd60`](#insn-004cdd60) → [`004cdd64`](#insn-004cdd64)
- ブロック [`004cdd64`](#insn-004cdd64) 範囲 `[['004cdd64', '004cdd97']]`
  - `CONDITIONAL_JUMP` [`004cdd94`](#insn-004cdd94) → [`004cddac`](#insn-004cddac)
  - `FALL_THROUGH` [`004cdd94`](#insn-004cdd94) → [`004cdd98`](#insn-004cdd98)
- ブロック [`004cdd98`](#insn-004cdd98) 範囲 `[['004cdd98', '004cddab']]`
  - `CONDITIONAL_JUMP` [`004cdda8`](#insn-004cdda8) → [`004cdeec`](#insn-004cdeec)
  - `FALL_THROUGH` [`004cdda8`](#insn-004cdda8) → [`004cddac`](#insn-004cddac)
- ブロック [`004cddac`](#insn-004cddac) 範囲 `[['004cddac', '004cddd3']]`
  - `CONDITIONAL_JUMP` [`004cddd0`](#insn-004cddd0) → [`004cde1c`](#insn-004cde1c)
  - `FALL_THROUGH` [`004cddd0`](#insn-004cddd0) → [`004cddd4`](#insn-004cddd4)
- ブロック [`004cddd4`](#insn-004cddd4) 範囲 `[['004cddd4', '004cddd7']]`
  - `CONDITIONAL_JUMP` [`004cddd4`](#insn-004cddd4) → [`004cdf10`](#insn-004cdf10)
  - `FALL_THROUGH` [`004cddd4`](#insn-004cddd4) → [`004cddd8`](#insn-004cddd8)
- ブロック [`004cddd8`](#insn-004cddd8) 範囲 `[['004cddd8', '004cde17']]`
  - `CONDITIONAL_JUMP` [`004cde14`](#insn-004cde14) → [`004cde28`](#insn-004cde28)
  - `FALL_THROUGH` [`004cde14`](#insn-004cde14) → [`004cde18`](#insn-004cde18)
- ブロック [`004cde18`](#insn-004cde18) 範囲 `[['004cde18', '004cde1b']]`
  - `UNCONDITIONAL_JUMP` [`004cde18`](#insn-004cde18) → [`004cde4c`](#insn-004cde4c)
- ブロック [`004cde1c`](#insn-004cde1c) 範囲 `[['004cde1c', '004cde27']]`
  - `CONDITIONAL_JUMP` [`004cde24`](#insn-004cde24) → [`004cde4c`](#insn-004cde4c)
  - `FALL_THROUGH` [`004cde24`](#insn-004cde24) → [`004cde28`](#insn-004cde28)
- ブロック [`004cde28`](#insn-004cde28) 範囲 `[['004cde28', '004cde4b']]`
  - `FALL_THROUGH` [`004cde48`](#insn-004cde48) → [`004cde4c`](#insn-004cde4c)
- ブロック [`004cde4c`](#insn-004cde4c) 範囲 `[['004cde4c', '004cde57']]`
  - `CONDITIONAL_JUMP` [`004cde54`](#insn-004cde54) → [`004cde78`](#insn-004cde78)
  - `FALL_THROUGH` [`004cde54`](#insn-004cde54) → [`004cde58`](#insn-004cde58)
- ブロック [`004cde58`](#insn-004cde58) 範囲 `[['004cde58', '004cde73']]`
  - `CONDITIONAL_JUMP` [`004cde70`](#insn-004cde70) → [`004cde80`](#insn-004cde80)
  - `FALL_THROUGH` [`004cde70`](#insn-004cde70) → [`004cde74`](#insn-004cde74)
- ブロック [`004cde74`](#insn-004cde74) 範囲 `[['004cde74', '004cde77']]`
  - `UNCONDITIONAL_JUMP` [`004cde74`](#insn-004cde74) → [`004cde88`](#insn-004cde88)
- ブロック [`004cde78`](#insn-004cde78) 範囲 `[['004cde78', '004cde7f']]`
  - `CONDITIONAL_JUMP` [`004cde7c`](#insn-004cde7c) → [`004cde88`](#insn-004cde88)
  - `FALL_THROUGH` [`004cde7c`](#insn-004cde7c) → [`004cde80`](#insn-004cde80)
- ブロック [`004cde80`](#insn-004cde80) 範囲 `[['004cde80', '004cde87']]`
  - `FALL_THROUGH` [`004cde84`](#insn-004cde84) → [`004cde88`](#insn-004cde88)
- ブロック [`004cde88`](#insn-004cde88) 範囲 `[['004cde88', '004cde8f']]`
  - `CONDITIONAL_JUMP` [`004cde8c`](#insn-004cde8c) → [`004cde9c`](#insn-004cde9c)
  - `FALL_THROUGH` [`004cde8c`](#insn-004cde8c) → [`004cde90`](#insn-004cde90)
- ブロック [`004cde90`](#insn-004cde90) 範囲 `[['004cde90', '004cde9b']]`
  - `FALL_THROUGH` [`004cde98`](#insn-004cde98) → [`004cde9c`](#insn-004cde9c)
- ブロック [`004cde9c`](#insn-004cde9c) 範囲 `[['004cde9c', '004cde9f']]`
  - `CONDITIONAL_JUMP` [`004cde9c`](#insn-004cde9c) → [`004cdea8`](#insn-004cdea8)
  - `FALL_THROUGH` [`004cde9c`](#insn-004cde9c) → [`004cdea0`](#insn-004cdea0)
- ブロック [`004cdea0`](#insn-004cdea0) 範囲 `[['004cdea0', '004cdea7']]`
  - `FALL_THROUGH` [`004cdea4`](#insn-004cdea4) → [`004cdea8`](#insn-004cdea8)
- ブロック [`004cdea8`](#insn-004cdea8) 範囲 `[['004cdea8', '004cdec7']]`
  - `CONDITIONAL_JUMP` [`004cdec4`](#insn-004cdec4) → [`004cdfdc`](#insn-004cdfdc)
  - `FALL_THROUGH` [`004cdec4`](#insn-004cdec4) → [`004cdec8`](#insn-004cdec8)
- ブロック [`004cdec8`](#insn-004cdec8) 範囲 `[['004cdec8', '004cdeeb']]`
- ブロック [`004cdeec`](#insn-004cdeec) 範囲 `[['004cdeec', '004cdef3']]`
  - `CONDITIONAL_JUMP` [`004cdef0`](#insn-004cdef0) → [`004cde90`](#insn-004cde90)
  - `FALL_THROUGH` [`004cdef0`](#insn-004cdef0) → [`004cdef4`](#insn-004cdef4)
- ブロック [`004cdef4`](#insn-004cdef4) 範囲 `[['004cdef4', '004cdef7']]`
  - `UNCONDITIONAL_JUMP` [`004cdef4`](#insn-004cdef4) → [`004cde9c`](#insn-004cde9c)
- ブロック [`004cdef8`](#insn-004cdef8) 範囲 `[['004cdef8', '004cdf07']]`
  - `CONDITIONAL_JUMP` [`004cdf04`](#insn-004cdf04) → [`004cdfdc`](#insn-004cdfdc)
  - `FALL_THROUGH` [`004cdf04`](#insn-004cdf04) → [`004cdf08`](#insn-004cdf08)
- ブロック [`004cdf08`](#insn-004cdf08) 範囲 `[['004cdf08', '004cdf0f']]`
- ブロック [`004cdf10`](#insn-004cdf10) 範囲 `[['004cdf10', '004cdf1f']]`
  - `CONDITIONAL_JUMP` [`004cdf1c`](#insn-004cdf1c) → [`004cdfdc`](#insn-004cdfdc)
  - `FALL_THROUGH` [`004cdf1c`](#insn-004cdf1c) → [`004cdf20`](#insn-004cdf20)
- ブロック [`004cdf20`](#insn-004cdf20) 範囲 `[['004cdf20', '004cdf27']]`
- ブロック [`004cdfdc`](#insn-004cdfdc) 範囲 `[['004cdfdc', '004cdfdf']]`

## 命令位置別の参照

- [`004cdbf0`](#insn-004cdbf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdbf4`](#insn-004cdbf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdbf8`](#insn-004cdbf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdbfc`](#insn-004cdbfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc00`](#insn-004cdc00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc04`](#insn-004cdc04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc20`](#insn-004cdc20) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc24`](#insn-004cdc24) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc38`](#insn-004cdc38) → [`00c58dd0`](../00c58/00c58dd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58dd0` · 推定シンボル `None` · 推定型 `None`
- [`004cdc3c`](#insn-004cdc3c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc40`](#insn-004cdc40) → [`004cdc4c`](#insn-004cdc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc44`](#insn-004cdc44) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc48`](#insn-004cdc48) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004cdc4c`](#insn-004cdc4c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc64`](#insn-004cdc64) → [`00c58de0`](../00c58/00c58de0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58de0` · 推定シンボル `None` · 推定型 `None`
- [`004cdc68`](#insn-004cdc68) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc6c`](#insn-004cdc6c) → [`004cdc78`](#insn-004cdc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc70`](#insn-004cdc70) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc74`](#insn-004cdc74) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004cdc78`](#insn-004cdc78) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc8c`](#insn-004cdc8c) → [`004cdc98`](#insn-004cdc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc94`](#insn-004cdc94) → [`004cdea8`](#insn-004cdea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdc98`](#insn-004cdc98) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdcb4`](#insn-004cdcb4) → [`004b34c8`](../004b3/004b34c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b34c8` · 推定シンボル `None` · 推定型 `None`
- [`004cdcbc`](#insn-004cdcbc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdcd0`](#insn-004cdcd0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdcd4`](#insn-004cdcd4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdcd8`](#insn-004cdcd8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdce0`](#insn-004cdce0) → [`004cdd30`](#insn-004cdd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdce4`](#insn-004cdce4) → [`004cdef8`](#insn-004cdef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdcec`](#insn-004cdcec) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`004cdd00`](#insn-004cdd00) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd04`](#insn-004cdd04) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd08`](#insn-004cdd08) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`004cdd18`](#insn-004cdd18) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd1c`](#insn-004cdd1c) → [`00c57b40`](../00c57/00c57b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b40` · 推定シンボル `None` · 推定型 `None`
- [`004cdd20`](#insn-004cdd20) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd28`](#insn-004cdd28) → [`004cdd40`](#insn-004cdd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd2c`](#insn-004cdd2c) → [`004cdd64`](#insn-004cdd64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd3c`](#insn-004cdd3c) → [`004cdd64`](#insn-004cdd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd40`](#insn-004cdd40) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd44`](#insn-004cdd44) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd48`](#insn-004cdd48) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cdd58`](#insn-004cdd58) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004cdd60`](#insn-004cdd60) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004cdd64`](#insn-004cdd64) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd88`](#insn-004cdd88) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdd94`](#insn-004cdd94) → [`004cddac`](#insn-004cddac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdda4`](#insn-004cdda4) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`004cdda8`](#insn-004cdda8) → [`004cdeec`](#insn-004cdeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddbc`](#insn-004cddbc) → [`00c58df0`](../00c58/00c58df0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58df0` · 推定シンボル `None` · 推定型 `None`
- [`004cddc0`](#insn-004cddc0) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddc4`](#insn-004cddc4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddc8`](#insn-004cddc8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddd0`](#insn-004cddd0) → [`004cde1c`](#insn-004cde1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddd4`](#insn-004cddd4) → [`004cdf10`](#insn-004cdf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdddc`](#insn-004cdddc) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`004cddf0`](#insn-004cddf0) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddf4`](#insn-004cddf4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cddf8`](#insn-004cddf8) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`004cde08`](#insn-004cde08) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde0c`](#insn-004cde0c) → [`00c57b40`](../00c57/00c57b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b40` · 推定シンボル `None` · 推定型 `None`
- [`004cde10`](#insn-004cde10) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde14`](#insn-004cde14) → [`004cde28`](#insn-004cde28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde18`](#insn-004cde18) → [`004cde4c`](#insn-004cde4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde24`](#insn-004cde24) → [`004cde4c`](#insn-004cde4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde28`](#insn-004cde28) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde2c`](#insn-004cde2c) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde30`](#insn-004cde30) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cde40`](#insn-004cde40) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004cde48`](#insn-004cde48) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004cde54`](#insn-004cde54) → [`004cde78`](#insn-004cde78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde64`](#insn-004cde64) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`004cde70`](#insn-004cde70) → [`004cde80`](#insn-004cde80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde74`](#insn-004cde74) → [`004cde88`](#insn-004cde88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde7c`](#insn-004cde7c) → [`004cde88`](#insn-004cde88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde84`](#insn-004cde84) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004cde88`](#insn-004cde88) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde8c`](#insn-004cde8c) → [`004cde9c`](#insn-004cde9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde94`](#insn-004cde94) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cde98`](#insn-004cde98) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004cde9c`](#insn-004cde9c) → [`004cdea8`](#insn-004cdea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdea4`](#insn-004cdea4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004cdeac`](#insn-004cdeac) → [`00c58e00`](../00c58/00c58e00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58e00` · 推定シンボル `None` · 推定型 `None`
- [`004cdeb4`](#insn-004cdeb4) → [`00c58e10`](../00c58/00c58e10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58e10` · 推定シンボル `None` · 推定型 `None`
- [`004cdebc`](#insn-004cdebc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdec4`](#insn-004cdec4) → [`004cdfdc`](#insn-004cdfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdecc`](#insn-004cdecc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cded0`](#insn-004cded0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cded4`](#insn-004cded4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cded8`](#insn-004cded8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdedc`](#insn-004cdedc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdee0`](#insn-004cdee0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdef0`](#insn-004cdef0) → [`004cde90`](#insn-004cde90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdef4`](#insn-004cdef4) → [`004cde9c`](#insn-004cde9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdefc`](#insn-004cdefc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdf04`](#insn-004cdf04) → [`004cdfdc`](#insn-004cdfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdf0c`](#insn-004cdf0c) → [`0049f3ec`](../0049f/0049f3ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3ec` · 推定シンボル `None` · 推定型 `None`
- [`004cdf14`](#insn-004cdf14) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdf1c`](#insn-004cdf1c) → [`004cdfdc`](#insn-004cdfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cdf24`](#insn-004cdf24) → [`0049f3ec`](../0049f/0049f3ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3ec` · 推定シンボル `None` · 推定型 `None`
- [`004cdfdc`](#insn-004cdfdc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cdbf0`](#insn-004cdbf0)

~~~json
{
  "source": "004cdbf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdbf4`](#insn-004cdbf4)

~~~json
{
  "source": "004cdbf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdbf8`](#insn-004cdbf8)

~~~json
{
  "source": "004cdbf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdbfc`](#insn-004cdbfc)

~~~json
{
  "source": "004cdbfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc00`](#insn-004cdc00)

~~~json
{
  "source": "004cdc00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc04`](#insn-004cdc04)

~~~json
{
  "source": "004cdc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc20`](#insn-004cdc20)

~~~json
{
  "source": "004cdc20",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc24`](#insn-004cdc24)

~~~json
{
  "source": "004cdc24",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc38`](#insn-004cdc38)

~~~json
{
  "source": "004cdc38",
  "target": "00c58dd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdc3c`](#insn-004cdc3c)

~~~json
{
  "source": "004cdc3c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc40`](#insn-004cdc40)

~~~json
{
  "source": "004cdc40",
  "target": "004cdc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc44`](#insn-004cdc44)

~~~json
{
  "source": "004cdc44",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc48`](#insn-004cdc48)

~~~json
{
  "source": "004cdc48",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdc4c`](#insn-004cdc4c)

~~~json
{
  "source": "004cdc4c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc64`](#insn-004cdc64)

~~~json
{
  "source": "004cdc64",
  "target": "00c58de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdc68`](#insn-004cdc68)

~~~json
{
  "source": "004cdc68",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc6c`](#insn-004cdc6c)

~~~json
{
  "source": "004cdc6c",
  "target": "004cdc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc70`](#insn-004cdc70)

~~~json
{
  "source": "004cdc70",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc74`](#insn-004cdc74)

~~~json
{
  "source": "004cdc74",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdc78`](#insn-004cdc78)

~~~json
{
  "source": "004cdc78",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc8c`](#insn-004cdc8c)

~~~json
{
  "source": "004cdc8c",
  "target": "004cdc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc94`](#insn-004cdc94)

~~~json
{
  "source": "004cdc94",
  "target": "004cdea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdc98`](#insn-004cdc98)

~~~json
{
  "source": "004cdc98",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdcb4`](#insn-004cdcb4)

~~~json
{
  "source": "004cdcb4",
  "target": "004b34c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdcbc`](#insn-004cdcbc)

~~~json
{
  "source": "004cdcbc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdcd0`](#insn-004cdcd0)

~~~json
{
  "source": "004cdcd0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdcd4`](#insn-004cdcd4)

~~~json
{
  "source": "004cdcd4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdcd8`](#insn-004cdcd8)

~~~json
{
  "source": "004cdcd8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdce0`](#insn-004cdce0)

~~~json
{
  "source": "004cdce0",
  "target": "004cdd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdce4`](#insn-004cdce4)

~~~json
{
  "source": "004cdce4",
  "target": "004cdef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdcec`](#insn-004cdcec)

~~~json
{
  "source": "004cdcec",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdd00`](#insn-004cdd00)

~~~json
{
  "source": "004cdd00",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd04`](#insn-004cdd04)

~~~json
{
  "source": "004cdd04",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd08`](#insn-004cdd08)

~~~json
{
  "source": "004cdd08",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdd18`](#insn-004cdd18)

~~~json
{
  "source": "004cdd18",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd1c`](#insn-004cdd1c)

~~~json
{
  "source": "004cdd1c",
  "target": "00c57b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdd20`](#insn-004cdd20)

~~~json
{
  "source": "004cdd20",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd28`](#insn-004cdd28)

~~~json
{
  "source": "004cdd28",
  "target": "004cdd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd2c`](#insn-004cdd2c)

~~~json
{
  "source": "004cdd2c",
  "target": "004cdd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd3c`](#insn-004cdd3c)

~~~json
{
  "source": "004cdd3c",
  "target": "004cdd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd40`](#insn-004cdd40)

~~~json
{
  "source": "004cdd40",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd44`](#insn-004cdd44)

~~~json
{
  "source": "004cdd44",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd48`](#insn-004cdd48)

~~~json
{
  "source": "004cdd48",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cdd58`](#insn-004cdd58)

~~~json
{
  "source": "004cdd58",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdd60`](#insn-004cdd60)

~~~json
{
  "source": "004cdd60",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdd64`](#insn-004cdd64)

~~~json
{
  "source": "004cdd64",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd88`](#insn-004cdd88)

~~~json
{
  "source": "004cdd88",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdd94`](#insn-004cdd94)

~~~json
{
  "source": "004cdd94",
  "target": "004cddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdda4`](#insn-004cdda4)

~~~json
{
  "source": "004cdda4",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdda8`](#insn-004cdda8)

~~~json
{
  "source": "004cdda8",
  "target": "004cdeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddbc`](#insn-004cddbc)

~~~json
{
  "source": "004cddbc",
  "target": "00c58df0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cddc0`](#insn-004cddc0)

~~~json
{
  "source": "004cddc0",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddc4`](#insn-004cddc4)

~~~json
{
  "source": "004cddc4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddc8`](#insn-004cddc8)

~~~json
{
  "source": "004cddc8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddd0`](#insn-004cddd0)

~~~json
{
  "source": "004cddd0",
  "target": "004cde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddd4`](#insn-004cddd4)

~~~json
{
  "source": "004cddd4",
  "target": "004cdf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdddc`](#insn-004cdddc)

~~~json
{
  "source": "004cdddc",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cddf0`](#insn-004cddf0)

~~~json
{
  "source": "004cddf0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddf4`](#insn-004cddf4)

~~~json
{
  "source": "004cddf4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cddf8`](#insn-004cddf8)

~~~json
{
  "source": "004cddf8",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde08`](#insn-004cde08)

~~~json
{
  "source": "004cde08",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde0c`](#insn-004cde0c)

~~~json
{
  "source": "004cde0c",
  "target": "00c57b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde10`](#insn-004cde10)

~~~json
{
  "source": "004cde10",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde14`](#insn-004cde14)

~~~json
{
  "source": "004cde14",
  "target": "004cde28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde18`](#insn-004cde18)

~~~json
{
  "source": "004cde18",
  "target": "004cde4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde24`](#insn-004cde24)

~~~json
{
  "source": "004cde24",
  "target": "004cde4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde28`](#insn-004cde28)

~~~json
{
  "source": "004cde28",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde2c`](#insn-004cde2c)

~~~json
{
  "source": "004cde2c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde30`](#insn-004cde30)

~~~json
{
  "source": "004cde30",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cde40`](#insn-004cde40)

~~~json
{
  "source": "004cde40",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde48`](#insn-004cde48)

~~~json
{
  "source": "004cde48",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde54`](#insn-004cde54)

~~~json
{
  "source": "004cde54",
  "target": "004cde78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde64`](#insn-004cde64)

~~~json
{
  "source": "004cde64",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde70`](#insn-004cde70)

~~~json
{
  "source": "004cde70",
  "target": "004cde80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde74`](#insn-004cde74)

~~~json
{
  "source": "004cde74",
  "target": "004cde88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde7c`](#insn-004cde7c)

~~~json
{
  "source": "004cde7c",
  "target": "004cde88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde84`](#insn-004cde84)

~~~json
{
  "source": "004cde84",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde88`](#insn-004cde88)

~~~json
{
  "source": "004cde88",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde8c`](#insn-004cde8c)

~~~json
{
  "source": "004cde8c",
  "target": "004cde9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde94`](#insn-004cde94)

~~~json
{
  "source": "004cde94",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cde98`](#insn-004cde98)

~~~json
{
  "source": "004cde98",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cde9c`](#insn-004cde9c)

~~~json
{
  "source": "004cde9c",
  "target": "004cdea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdea4`](#insn-004cdea4)

~~~json
{
  "source": "004cdea4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdeac`](#insn-004cdeac)

~~~json
{
  "source": "004cdeac",
  "target": "00c58e00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdeb4`](#insn-004cdeb4)

~~~json
{
  "source": "004cdeb4",
  "target": "00c58e10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdebc`](#insn-004cdebc)

~~~json
{
  "source": "004cdebc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdec4`](#insn-004cdec4)

~~~json
{
  "source": "004cdec4",
  "target": "004cdfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdecc`](#insn-004cdecc)

~~~json
{
  "source": "004cdecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cded0`](#insn-004cded0)

~~~json
{
  "source": "004cded0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cded4`](#insn-004cded4)

~~~json
{
  "source": "004cded4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cded8`](#insn-004cded8)

~~~json
{
  "source": "004cded8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdedc`](#insn-004cdedc)

~~~json
{
  "source": "004cdedc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdee0`](#insn-004cdee0)

~~~json
{
  "source": "004cdee0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdef0`](#insn-004cdef0)

~~~json
{
  "source": "004cdef0",
  "target": "004cde90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdef4`](#insn-004cdef4)

~~~json
{
  "source": "004cdef4",
  "target": "004cde9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdefc`](#insn-004cdefc)

~~~json
{
  "source": "004cdefc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdf04`](#insn-004cdf04)

~~~json
{
  "source": "004cdf04",
  "target": "004cdfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdf0c`](#insn-004cdf0c)

~~~json
{
  "source": "004cdf0c",
  "target": "0049f3ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdf14`](#insn-004cdf14)

~~~json
{
  "source": "004cdf14",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdf1c`](#insn-004cdf1c)

~~~json
{
  "source": "004cdf1c",
  "target": "004cdfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cdf24`](#insn-004cdf24)

~~~json
{
  "source": "004cdf24",
  "target": "0049f3ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cdfdc`](#insn-004cdfdc)

~~~json
{
  "source": "004cdfdc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
