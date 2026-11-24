# 004ffaac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004ffa6c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0011.md#compare-2e4af4e0de5092a70159474fa52ca69d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004ffaec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0011.md#compare-eafc4c9e90bf5f5944a050e572aab298)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ffaac",
  "name": "FUN_004ffaac",
  "size": 820,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "020be7024c55513b83475a71a74dba2c74bb91b4617e20605f29b594d23dc780",
  "source_text_sha256": "020be7024c55513b83475a71a74dba2c74bb91b4617e20605f29b594d23dc780",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ffaac",
        "004ffddb"
      ],
      [
        "004ffe1c",
        "004ffe1f"
      ]
    ],
    "bytes_sha256": "451587dbcff03bc5b184e3e03741b17229cc9bc3b485e4b692ae0438b2f578af",
    "instruction_count": 205,
    "instruction_bytes": 820,
    "body_bytes": 820,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ff838](../004ff/004ff838.md)

## 呼び出し先

- [005085bc](../00508/005085bc.md)
- [00514da4](../00514/00514da4.md)
- [0053af90](../0053a/0053af90.md)
- [00548098](../00548/00548098.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c581c0](../00c58/00c581c0.md)
- [00c58820](../00c58/00c58820.md)
- [00c59900](../00c59/00c59900.md)
- [00c59960](../00c59/00c59960.md)
- [00c59990](../00c59/00c59990.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5945 bytes

~~~c

void FUN_004ffaac(undefined8 param_1,undefined8 param_2,byte *param_3,undefined4 param_4)

{
  byte *pbVar1;
  undefined8 *puVar2;
  undefined *puVar3;
  byte *pbVar4;
  ulong uVar5;
  undefined8 uVar6;
  void *pvVar7;
  byte bVar8;
  long lVar9;
  undefined1 *puVar10;
  bool bVar11;
  uint uVar12;
  long *plVar13;
  long *plVar14;
  long lVar15;
  long *plVar16;
  undefined1 auVar17 [16];
  undefined8 *local_1c0;
  undefined8 *puStack_1b8;
  undefined8 local_1b0;
  undefined8 uStack_1a8;
  void *local_1a0;
  void *local_198;
  undefined8 uStack_190;
  long local_188;
  void *local_180;
  void *local_178;
  undefined *puStack_170;
  byte local_168;
  undefined1 auStack_167 [7];
  ulong local_160;
  undefined1 *local_158;
  byte local_130;
  void *local_120;
  undefined1 auStack_108 [152];
  long local_70;
  
  lVar9 = tpidr_el0;
  local_70 = *(long *)(lVar9 + 0x28);
  auVar17 = FUN_00548098(param_2,param_3);
  if (auVar17._0_8_ != auVar17._8_8_) {
    pbVar1 = param_3 + 1;
    lVar15 = *(long *)
              PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac10
    ;
    uVar6 = *(undefined8 *)
             (
             PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac10
             + 0x40);
    pvVar7 = *(void **)(
                       PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac10
                       + 0x48);
    puVar2 = (undefined8 *)(PTR__ZTVN5Botan7X509_DNE_00c9b0d0 + 0x10);
    puVar3 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0 +
             0x10;
    plVar16 = auVar17._0_8_;
    do {
      bVar8 = *param_3;
      uVar5 = (ulong)(bVar8 >> 1);
      if ((bVar8 & 1) != 0) {
        uVar5 = *(ulong *)(param_3 + 8);
      }
      if (uVar5 == 2) {
        pbVar4 = pbVar1;
        if ((bVar8 & 1) != 0) {
          pbVar4 = *(byte **)(param_3 + 0x10);
        }
        if (*(short *)pbVar4 != 0x5049) {
          if (*(short *)pbVar4 == 0x4e44) {
            FUN_005085bc(&local_188,plVar16 + 7,0x18);
            local_1b0 = 0;
            uStack_1a8 = 0;
            local_198 = (void *)0x0;
            uStack_190 = 0;
            local_1a0 = (void *)0x0;
            local_1c0 = puVar2;
            puStack_1b8 = &local_1b0;
            _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE
                      (&local_188,&local_1c0);
            (*(code *)*local_1c0)(&local_1c0,param_1);
            if (local_1a0 != (void *)0x0) {
              local_198 = local_1a0;
              _ZdlPv(local_1a0);
            }
            FUN_0053af90(&puStack_1b8,local_1b0);
            local_188 = lVar15;
            *(undefined8 *)((long)&local_188 + *(long *)(lVar15 + -0x18)) = uVar6;
            local_178 = pvVar7;
            puStack_170 = puVar3;
            if ((local_130 & 1) != 0) {
              _ZdlPv(local_120);
            }
            _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(&puStack_170);
            _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED2Ev
                      (&local_188,
                       PTR__ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac10
                       + 8);
            _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_108);
          }
          goto LAB_004ffd48;
        }
        uVar12 = _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
                           (plVar16 + 7);
        uVar12 = (uVar12 & 0xff00ff00) >> 8 | (uVar12 & 0xff00ff) << 8;
        local_188 = CONCAT44(local_188._4_4_,uVar12 >> 0x10 | uVar12 << 0x10);
        _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm(param_1,param_4,0x80,&local_188,4);
        plVar14 = (long *)plVar16[1];
        if ((long *)plVar16[1] != (long *)0x0) goto LAB_004ffd50;
LAB_004ffd90:
        do {
          plVar13 = (long *)plVar16[2];
          bVar11 = (long *)*plVar13 != plVar16;
          plVar16 = plVar13;
        } while (bVar11);
      }
      else {
        if (uVar5 == 3) {
          pbVar4 = pbVar1;
          if ((bVar8 & 1) != 0) {
            pbVar4 = *(byte **)(param_3 + 0x10);
          }
          if ((*(short *)pbVar4 != 0x4e44 || pbVar4[2] != 0x53) &&
             (*(short *)pbVar4 != 0x5255 || pbVar4[2] != 0x49)) goto LAB_004ffd48;
LAB_004ffc04:
          _ZN5Botan11ASN1_StringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE
                    (&local_188,plVar16 + 7,0x16);
          uVar5 = (ulong)(local_168 >> 1);
          puVar10 = auStack_167;
          if ((local_168 & 1) != 0) {
            uVar5 = local_160;
            puVar10 = local_158;
          }
          _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm
                    (param_1,param_4,0x80,puVar10,uVar5);
          if ((local_168 & 1) != 0) {
            _ZdlPv(local_158);
          }
          if (local_180 == (void *)0x0) goto LAB_004ffd48;
          local_178 = local_180;
          _ZdlPv(local_180);
          plVar14 = (long *)plVar16[1];
        }
        else {
          if (uVar5 == 6) {
            pbVar4 = pbVar1;
            if ((bVar8 & 1) != 0) {
              pbVar4 = *(byte **)(param_3 + 0x10);
            }
            if (*(int *)pbVar4 == 0x38434652 && *(short *)(pbVar4 + 4) == 0x3232) goto LAB_004ffc04;
          }
LAB_004ffd48:
          plVar14 = (long *)plVar16[1];
        }
        if (plVar14 == (long *)0x0) goto LAB_004ffd90;
LAB_004ffd50:
        do {
          plVar13 = plVar14;
          plVar14 = (long *)*plVar13;
        } while ((long *)*plVar13 != (long *)0x0);
      }
      plVar16 = plVar13;
    } while (plVar13 != auVar17._8_8_);
  }
  if (*(long *)(lVar9 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ffaac"></a> `004ffaac` | `ff c3 07 d1` | sub sp,sp,#0x1f0 | `FALL_THROUGH`
<a id="insn-004ffab0"></a> `004ffab0` | `fd 7b 19 a9` | stp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-004ffab4"></a> `004ffab4` | `fc 6f 1a a9` | stp x28,x27,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-004ffab8"></a> `004ffab8` | `fa 67 1b a9` | stp x26,x25,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-004ffabc"></a> `004ffabc` | `f8 5f 1c a9` | stp x24,x23,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-004ffac0"></a> `004ffac0` | `f6 57 1d a9` | stp x22,x21,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-004ffac4"></a> `004ffac4` | `f4 4f 1e a9` | stp x20,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-004ffac8"></a> `004ffac8` | `fd 43 06 91` | add x29,sp,#0x190 | `FALL_THROUGH`
<a id="insn-004ffacc"></a> `004ffacc` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004ffad0"></a> `004ffad0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004ffad4"></a> `004ffad4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-004ffad8"></a> `004ffad8` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004ffadc"></a> `004ffadc` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-004ffae0"></a> `004ffae0` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-004ffae4"></a> `004ffae4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004ffae8"></a> `004ffae8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-004ffaec"></a> `004ffaec` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004ffaf0"></a> `004ffaf0` | `6a 21 01 94` | bl 0x00548098 | `UNCONDITIONAL_CALL`
<a id="insn-004ffaf4"></a> `004ffaf4` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-004ffaf8"></a> `004ffaf8` | `80 15 00 54` | b.eq 0x004ffda8 | `CONDITIONAL_JUMP`
<a id="insn-004ffafc"></a> `004ffafc` | `c8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ffb00"></a> `004ffb00` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffb04"></a> `004ffb04` | `ea a3 01 91` | add x10,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffb08"></a> `004ffb08` | `08 09 46 f9` | ldr x8,[x8, #0xc10] | `FALL_THROUGH`
<a id="insn-004ffb0c"></a> `004ffb0c` | `39 41 00 91` | add x25,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004ffb10"></a> `004ffb10` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-004ffb14"></a> `004ffb14` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004ffb18"></a> `004ffb18` | `9a 06 00 91` | add x26,x20,#0x1 | `FALL_THROUGH`
<a id="insn-004ffb1c"></a> `004ffb1c` | `58 85 00 91` | add x24,x10,#0x21 | `FALL_THROUGH`
<a id="insn-004ffb20"></a> `004ffb20` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-004ffb24"></a> `004ffb24` | `09 21 44 a9` | ldp x9,x8,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-004ffb28"></a> `004ffb28` | `3c 09 8a 52` | mov w28,#0x5049 | `FALL_THROUGH`
<a id="insn-004ffb2c"></a> `004ffb2c` | `9b c8 89 52` | mov w27,#0x4e44 | `FALL_THROUGH`
<a id="insn-004ffb30"></a> `004ffb30` | `e9 2f 01 a9` | stp x9,x11,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ffb34"></a> `004ffb34` | `c9 3c 00 f0` | adrp x9,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ffb38"></a> `004ffb38` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ffb3c"></a> `004ffb3c` | `e8 3c 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004ffb40"></a> `004ffb40` | `08 69 40 f9` | ldr x8,[x8, #0xd0] | `FALL_THROUGH`
<a id="insn-004ffb44"></a> `004ffb44` | `29 e1 45 f9` | ldr x9,[x9, #0xbc0] | `FALL_THROUGH`
<a id="insn-004ffb48"></a> `004ffb48` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004ffb4c"></a> `004ffb4c` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ffb50"></a> `004ffb50` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004ffb54"></a> `004ffb54` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-004ffb58"></a> `004ffb58` | `04 00 00 14` | b 0x004ffb68 | `UNCONDITIONAL_JUMP`
<a id="insn-004ffb5c"></a> `004ffb5c` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-004ffb60"></a> `004ffb60` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-004ffb64"></a> `004ffb64` | `20 12 00 54` | b.eq 0x004ffda8 | `CONDITIONAL_JUMP`
<a id="insn-004ffb68"></a> `004ffb68` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004ffb6c"></a> `004ffb6c` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004ffb70"></a> `004ffb70` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffb74"></a> `004ffb74` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffb78"></a> `004ffb78` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ffb7c"></a> `004ffb7c` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-004ffb80"></a> `004ffb80` | `40 07 00 54` | b.eq 0x004ffc68 | `CONDITIONAL_JUMP`
<a id="insn-004ffb84"></a> `004ffb84` | `3f 0d 00 f1` | cmp x9,#0x3 | `FALL_THROUGH`
<a id="insn-004ffb88"></a> `004ffb88` | `e0 01 00 54` | b.eq 0x004ffbc4 | `CONDITIONAL_JUMP`
<a id="insn-004ffb8c"></a> `004ffb8c` | `3f 19 00 f1` | cmp x9,#0x6 | `FALL_THROUGH`
<a id="insn-004ffb90"></a> `004ffb90` | `c1 0d 00 54` | b.ne 0x004ffd48 | `CONDITIONAL_JUMP`
<a id="insn-004ffb94"></a> `004ffb94` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004ffb98"></a> `004ffb98` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffb9c"></a> `004ffb9c` | `4a ca 88 52` | mov w10,#0x4652 | `FALL_THROUGH`
<a id="insn-004ffba0"></a> `004ffba0` | `6a 08 a7 72` | movk w10,#0x3843, LSL #16 | `FALL_THROUGH`
<a id="insn-004ffba4"></a> `004ffba4` | `48 03 89 9a` | csel x8,x26,x9,eq | `FALL_THROUGH`
<a id="insn-004ffba8"></a> `004ffba8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffbac"></a> `004ffbac` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-004ffbb0"></a> `004ffbb0` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004ffbb4"></a> `004ffbb4` | `49 46 86 52` | mov w9,#0x3232 | `FALL_THROUGH`
<a id="insn-004ffbb8"></a> `004ffbb8` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ffbbc"></a> `004ffbbc` | `61 0c 00 54` | b.ne 0x004ffd48 | `CONDITIONAL_JUMP`
<a id="insn-004ffbc0"></a> `004ffbc0` | `11 00 00 14` | b 0x004ffc04 | `UNCONDITIONAL_JUMP`
<a id="insn-004ffbc4"></a> `004ffbc4` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004ffbc8"></a> `004ffbc8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffbcc"></a> `004ffbcc` | `48 03 89 9a` | csel x8,x26,x9,eq | `FALL_THROUGH`
<a id="insn-004ffbd0"></a> `004ffbd0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffbd4"></a> `004ffbd4` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-004ffbd8"></a> `004ffbd8` | `3f 01 1b 6b` | cmp w9,w27 | `FALL_THROUGH`
<a id="insn-004ffbdc"></a> `004ffbdc` | `69 0a 80 52` | mov w9,#0x53 | `FALL_THROUGH`
<a id="insn-004ffbe0"></a> `004ffbe0` | `40 01 49 7a` | ccmp w10,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ffbe4"></a> `004ffbe4` | `00 01 00 54` | b.eq 0x004ffc04 | `CONDITIONAL_JUMP`
<a id="insn-004ffbe8"></a> `004ffbe8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffbec"></a> `004ffbec` | `08 09 40 39` | ldrb w8,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-004ffbf0"></a> `004ffbf0` | `aa 4a 8a 52` | mov w10,#0x5255 | `FALL_THROUGH`
<a id="insn-004ffbf4"></a> `004ffbf4` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004ffbf8"></a> `004ffbf8` | `29 09 80 52` | mov w9,#0x49 | `FALL_THROUGH`
<a id="insn-004ffbfc"></a> `004ffbfc` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ffc00"></a> `004ffc00` | `41 0a 00 54` | b.ne 0x004ffd48 | `CONDITIONAL_JUMP`
<a id="insn-004ffc04"></a> `004ffc04` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffc08"></a> `004ffc08` | `e1 e2 00 91` | add x1,x23,#0x38 | `FALL_THROUGH`
<a id="insn-004ffc0c"></a> `004ffc0c` | `c2 02 80 52` | mov w2,#0x16 | `FALL_THROUGH`
<a id="insn-004ffc10"></a> `004ffc10` | `54 67 1d 94` | bl 0x00c59960 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc14"></a> `004ffc14` | `e8 23 42 39` | ldrb w8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-004ffc18"></a> `004ffc18` | `ea 27 49 a9` | ldp x10,x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004ffc1c"></a> `004ffc1c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffc20"></a> `004ffc20` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffc24"></a> `004ffc24` | `03 03 89 9a` | csel x3,x24,x9,eq | `FALL_THROUGH`
<a id="insn-004ffc28"></a> `004ffc28` | `64 01 8a 9a` | csel x4,x11,x10,eq | `FALL_THROUGH`
<a id="insn-004ffc2c"></a> `004ffc2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004ffc30"></a> `004ffc30` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-004ffc34"></a> `004ffc34` | `02 10 80 52` | mov w2,#0x80 | `FALL_THROUGH`
<a id="insn-004ffc38"></a> `004ffc38` | `fa 62 1d 94` | bl 0x00c58820 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc3c"></a> `004ffc3c` | `e8 23 42 39` | ldrb w8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-004ffc40"></a> `004ffc40` | `68 00 00 36` | tbz w8,#0x0,0x004ffc4c | `CONDITIONAL_JUMP`
<a id="insn-004ffc44"></a> `004ffc44` | `e0 4f 40 f9` | ldr x0,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-004ffc48"></a> `004ffc48` | `9a 60 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc4c"></a> `004ffc4c` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004ffc50"></a> `004ffc50` | `c0 07 00 b4` | cbz x0,0x004ffd48 | `CONDITIONAL_JUMP`
<a id="insn-004ffc54"></a> `004ffc54` | `e0 3f 00 f9` | str x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ffc58"></a> `004ffc58` | `96 60 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffc5c"></a> `004ffc5c` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-004ffc60"></a> `004ffc60` | `89 07 00 b5` | cbnz x9,0x004ffd50 | `CONDITIONAL_JUMP`
<a id="insn-004ffc64"></a> `004ffc64` | `4b 00 00 14` | b 0x004ffd90 | `UNCONDITIONAL_JUMP`
<a id="insn-004ffc68"></a> `004ffc68` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004ffc6c"></a> `004ffc6c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ffc70"></a> `004ffc70` | `48 03 89 9a` | csel x8,x26,x9,eq | `FALL_THROUGH`
<a id="insn-004ffc74"></a> `004ffc74` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-004ffc78"></a> `004ffc78` | `3f 01 1c 6b` | cmp w9,w28 | `FALL_THROUGH`
<a id="insn-004ffc7c"></a> `004ffc7c` | `20 07 00 54` | b.eq 0x004ffd60 | `CONDITIONAL_JUMP`
<a id="insn-004ffc80"></a> `004ffc80` | `08 01 40 79` | ldrh w8,[x8] | `FALL_THROUGH`
<a id="insn-004ffc84"></a> `004ffc84` | `1f 01 1b 6b` | cmp w8,w27 | `FALL_THROUGH`
<a id="insn-004ffc88"></a> `004ffc88` | `01 06 00 54` | b.ne 0x004ffd48 | `CONDITIONAL_JUMP`
<a id="insn-004ffc8c"></a> `004ffc8c` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffc90"></a> `004ffc90` | `e1 e2 00 91` | add x1,x23,#0x38 | `FALL_THROUGH`
<a id="insn-004ffc94"></a> `004ffc94` | `02 03 80 52` | mov w2,#0x18 | `FALL_THROUGH`
<a id="insn-004ffc98"></a> `004ffc98` | `49 22 00 94` | bl 0x005085bc | `UNCONDITIONAL_CALL`
<a id="insn-004ffc9c"></a> `004ffc9c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ffca0"></a> `004ffca0` | `fc c3 00 91` | add x28,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffca4"></a> `004ffca4` | `3f 7f 00 a9` | stp xzr,xzr,[x25] | `FALL_THROUGH`
<a id="insn-004ffca8"></a> `004ffca8` | `e8 67 03 a9` | stp x8,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004ffcac"></a> `004ffcac` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffcb0"></a> `004ffcb0` | `1f fd 02 a9` | stp xzr,xzr,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004ffcb4"></a> `004ffcb4` | `1f 01 02 f8` | stur xzr,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004ffcb8"></a> `004ffcb8` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffcbc"></a> `004ffcbc` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffcc0"></a> `004ffcc0` | `34 67 1d 94` | bl 0x00c59990 | `UNCONDITIONAL_CALL`
<a id="insn-004ffcc4"></a> `004ffcc4` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004ffcc8"></a> `004ffcc8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ffccc"></a> `004ffccc` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004ffcd0"></a> `004ffcd0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004ffcd4"></a> `004ffcd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ffcd8"></a> `004ffcd8` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ffcdc"></a> `004ffcdc` | `60 00 00 b4` | cbz x0,0x004ffce8 | `CONDITIONAL_JUMP`
<a id="insn-004ffce0"></a> `004ffce0` | `e0 2f 00 f9` | str x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-004ffce4"></a> `004ffce4` | `73 60 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffce8"></a> `004ffce8` | `e1 23 40 f9` | ldr x1,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ffcec"></a> `004ffcec` | `80 23 00 91` | add x0,x28,#0x8 | `FALL_THROUGH`
<a id="insn-004ffcf0"></a> `004ffcf0` | `a8 ec 00 94` | bl 0x0053af90 | `UNCONDITIONAL_CALL`
<a id="insn-004ffcf4"></a> `004ffcf4` | `e9 23 41 a9` | ldp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ffcf8"></a> `004ffcf8` | `fc a3 01 91` | add x28,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffcfc"></a> `004ffcfc` | `e8 37 00 f9` | str x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ffd00"></a> `004ffd00` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-004ffd04"></a> `004ffd04` | `89 6b 28 f8` | str x9,[x28, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004ffd08"></a> `004ffd08` | `e9 2b 40 a9` | ldp x9,x10,[sp] | `FALL_THROUGH`
<a id="insn-004ffd0c"></a> `004ffd0c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004ffd10"></a> `004ffd10` | `ea a7 07 a9` | stp x10,x9,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ffd14"></a> `004ffd14` | `68 00 00 36` | tbz w8,#0x0,0x004ffd20 | `CONDITIONAL_JUMP`
<a id="insn-004ffd18"></a> `004ffd18` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004ffd1c"></a> `004ffd1c` | `65 60 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd20"></a> `004ffd20` | `80 63 00 91` | add x0,x28,#0x18 | `FALL_THROUGH`
<a id="insn-004ffd24"></a> `004ffd24` | `9f 60 1d 94` | bl 0x00c57fa0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd28"></a> `004ffd28` | `c8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ffd2c"></a> `004ffd2c` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffd30"></a> `004ffd30` | `08 09 46 f9` | ldr x8,[x8, #0xc10] | `FALL_THROUGH`
<a id="insn-004ffd34"></a> `004ffd34` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004ffd38"></a> `004ffd38` | `22 61 1d 94` | bl 0x00c581c0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd3c"></a> `004ffd3c` | `80 03 02 91` | add x0,x28,#0x80 | `FALL_THROUGH`
<a id="insn-004ffd40"></a> `004ffd40` | `a0 60 1d 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd44"></a> `004ffd44` | `3c 09 8a 52` | mov w28,#0x5049 | `FALL_THROUGH`
<a id="insn-004ffd48"></a> `004ffd48` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-004ffd4c"></a> `004ffd4c` | `29 02 00 b4` | cbz x9,0x004ffd90 | `CONDITIONAL_JUMP`
<a id="insn-004ffd50"></a> `004ffd50` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-004ffd54"></a> `004ffd54` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-004ffd58"></a> `004ffd58` | `c9 ff ff b5` | cbnz x9,0x004ffd50 | `CONDITIONAL_JUMP`
<a id="insn-004ffd5c"></a> `004ffd5c` | `80 ff ff 17` | b 0x004ffb5c | `UNCONDITIONAL_JUMP`
<a id="insn-004ffd60"></a> `004ffd60` | `e0 e2 00 91` | add x0,x23,#0x38 | `FALL_THROUGH`
<a id="insn-004ffd64"></a> `004ffd64` | `e7 66 1d 94` | bl 0x00c59900 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd68"></a> `004ffd68` | `08 08 c0 5a` | rev w8,w0 | `FALL_THROUGH`
<a id="insn-004ffd6c"></a> `004ffd6c` | `e3 a3 01 91` | add x3,sp,#0x68 | `FALL_THROUGH`
<a id="insn-004ffd70"></a> `004ffd70` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004ffd74"></a> `004ffd74` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-004ffd78"></a> `004ffd78` | `02 10 80 52` | mov w2,#0x80 | `FALL_THROUGH`
<a id="insn-004ffd7c"></a> `004ffd7c` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-004ffd80"></a> `004ffd80` | `e8 6b 00 b9` | str w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ffd84"></a> `004ffd84` | `a7 62 1d 94` | bl 0x00c58820 | `UNCONDITIONAL_CALL`
<a id="insn-004ffd88"></a> `004ffd88` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-004ffd8c"></a> `004ffd8c` | `29 fe ff b5` | cbnz x9,0x004ffd50 | `CONDITIONAL_JUMP`
<a id="insn-004ffd90"></a> `004ffd90` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-004ffd94"></a> `004ffd94` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-004ffd98"></a> `004ffd98` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-004ffd9c"></a> `004ffd9c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-004ffda0"></a> `004ffda0` | `81 ff ff 54` | b.ne 0x004ffd90 | `CONDITIONAL_JUMP`
<a id="insn-004ffda4"></a> `004ffda4` | `6e ff ff 17` | b 0x004ffb5c | `UNCONDITIONAL_JUMP`
<a id="insn-004ffda8"></a> `004ffda8` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004ffdac"></a> `004ffdac` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004ffdb0"></a> `004ffdb0` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004ffdb4"></a> `004ffdb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ffdb8"></a> `004ffdb8` | `21 03 00 54` | b.ne 0x004ffe1c | `CONDITIONAL_JUMP`
<a id="insn-004ffdbc"></a> `004ffdbc` | `f4 4f 5e a9` | ldp x20,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-004ffdc0"></a> `004ffdc0` | `f6 57 5d a9` | ldp x22,x21,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-004ffdc4"></a> `004ffdc4` | `f8 5f 5c a9` | ldp x24,x23,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-004ffdc8"></a> `004ffdc8` | `fa 67 5b a9` | ldp x26,x25,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-004ffdcc"></a> `004ffdcc` | `fc 6f 5a a9` | ldp x28,x27,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-004ffdd0"></a> `004ffdd0` | `fd 7b 59 a9` | ldp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-004ffdd4"></a> `004ffdd4` | `ff c3 07 91` | add sp,sp,#0x1f0 | `FALL_THROUGH`
<a id="insn-004ffdd8"></a> `004ffdd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004ffe1c"></a> `004ffe1c` | `31 60 1d 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ffaac`](#insn-004ffaac) 範囲 `[['004ffaac', '004ffafb']]`
  - `CONDITIONAL_JUMP` [`004ffaf8`](#insn-004ffaf8) → [`004ffda8`](#insn-004ffda8)
  - `FALL_THROUGH` [`004ffaf8`](#insn-004ffaf8) → [`004ffafc`](#insn-004ffafc)
- ブロック [`004ffafc`](#insn-004ffafc) 範囲 `[['004ffafc', '004ffb5b']]`
  - `UNCONDITIONAL_JUMP` [`004ffb58`](#insn-004ffb58) → [`004ffb68`](#insn-004ffb68)
- ブロック [`004ffb5c`](#insn-004ffb5c) 範囲 `[['004ffb5c', '004ffb67']]`
  - `CONDITIONAL_JUMP` [`004ffb64`](#insn-004ffb64) → [`004ffda8`](#insn-004ffda8)
  - `FALL_THROUGH` [`004ffb64`](#insn-004ffb64) → [`004ffb68`](#insn-004ffb68)
- ブロック [`004ffb68`](#insn-004ffb68) 範囲 `[['004ffb68', '004ffb83']]`
  - `CONDITIONAL_JUMP` [`004ffb80`](#insn-004ffb80) → [`004ffc68`](#insn-004ffc68)
  - `FALL_THROUGH` [`004ffb80`](#insn-004ffb80) → [`004ffb84`](#insn-004ffb84)
- ブロック [`004ffb84`](#insn-004ffb84) 範囲 `[['004ffb84', '004ffb8b']]`
  - `CONDITIONAL_JUMP` [`004ffb88`](#insn-004ffb88) → [`004ffbc4`](#insn-004ffbc4)
  - `FALL_THROUGH` [`004ffb88`](#insn-004ffb88) → [`004ffb8c`](#insn-004ffb8c)
- ブロック [`004ffb8c`](#insn-004ffb8c) 範囲 `[['004ffb8c', '004ffb93']]`
  - `CONDITIONAL_JUMP` [`004ffb90`](#insn-004ffb90) → [`004ffd48`](#insn-004ffd48)
  - `FALL_THROUGH` [`004ffb90`](#insn-004ffb90) → [`004ffb94`](#insn-004ffb94)
- ブロック [`004ffb94`](#insn-004ffb94) 範囲 `[['004ffb94', '004ffbbf']]`
  - `CONDITIONAL_JUMP` [`004ffbbc`](#insn-004ffbbc) → [`004ffd48`](#insn-004ffd48)
  - `FALL_THROUGH` [`004ffbbc`](#insn-004ffbbc) → [`004ffbc0`](#insn-004ffbc0)
- ブロック [`004ffbc0`](#insn-004ffbc0) 範囲 `[['004ffbc0', '004ffbc3']]`
  - `UNCONDITIONAL_JUMP` [`004ffbc0`](#insn-004ffbc0) → [`004ffc04`](#insn-004ffc04)
- ブロック [`004ffbc4`](#insn-004ffbc4) 範囲 `[['004ffbc4', '004ffbe7']]`
  - `CONDITIONAL_JUMP` [`004ffbe4`](#insn-004ffbe4) → [`004ffc04`](#insn-004ffc04)
  - `FALL_THROUGH` [`004ffbe4`](#insn-004ffbe4) → [`004ffbe8`](#insn-004ffbe8)
- ブロック [`004ffbe8`](#insn-004ffbe8) 範囲 `[['004ffbe8', '004ffc03']]`
  - `CONDITIONAL_JUMP` [`004ffc00`](#insn-004ffc00) → [`004ffd48`](#insn-004ffd48)
  - `FALL_THROUGH` [`004ffc00`](#insn-004ffc00) → [`004ffc04`](#insn-004ffc04)
- ブロック [`004ffc04`](#insn-004ffc04) 範囲 `[['004ffc04', '004ffc43']]`
  - `CONDITIONAL_JUMP` [`004ffc40`](#insn-004ffc40) → [`004ffc4c`](#insn-004ffc4c)
  - `FALL_THROUGH` [`004ffc40`](#insn-004ffc40) → [`004ffc44`](#insn-004ffc44)
- ブロック [`004ffc44`](#insn-004ffc44) 範囲 `[['004ffc44', '004ffc4b']]`
  - `FALL_THROUGH` [`004ffc48`](#insn-004ffc48) → [`004ffc4c`](#insn-004ffc4c)
- ブロック [`004ffc4c`](#insn-004ffc4c) 範囲 `[['004ffc4c', '004ffc53']]`
  - `CONDITIONAL_JUMP` [`004ffc50`](#insn-004ffc50) → [`004ffd48`](#insn-004ffd48)
  - `FALL_THROUGH` [`004ffc50`](#insn-004ffc50) → [`004ffc54`](#insn-004ffc54)
- ブロック [`004ffc54`](#insn-004ffc54) 範囲 `[['004ffc54', '004ffc63']]`
  - `CONDITIONAL_JUMP` [`004ffc60`](#insn-004ffc60) → [`004ffd50`](#insn-004ffd50)
  - `FALL_THROUGH` [`004ffc60`](#insn-004ffc60) → [`004ffc64`](#insn-004ffc64)
- ブロック [`004ffc64`](#insn-004ffc64) 範囲 `[['004ffc64', '004ffc67']]`
  - `UNCONDITIONAL_JUMP` [`004ffc64`](#insn-004ffc64) → [`004ffd90`](#insn-004ffd90)
- ブロック [`004ffc68`](#insn-004ffc68) 範囲 `[['004ffc68', '004ffc7f']]`
  - `CONDITIONAL_JUMP` [`004ffc7c`](#insn-004ffc7c) → [`004ffd60`](#insn-004ffd60)
  - `FALL_THROUGH` [`004ffc7c`](#insn-004ffc7c) → [`004ffc80`](#insn-004ffc80)
- ブロック [`004ffc80`](#insn-004ffc80) 範囲 `[['004ffc80', '004ffc8b']]`
  - `CONDITIONAL_JUMP` [`004ffc88`](#insn-004ffc88) → [`004ffd48`](#insn-004ffd48)
  - `FALL_THROUGH` [`004ffc88`](#insn-004ffc88) → [`004ffc8c`](#insn-004ffc8c)
- ブロック [`004ffc8c`](#insn-004ffc8c) 範囲 `[['004ffc8c', '004ffcdf']]`
  - `CONDITIONAL_JUMP` [`004ffcdc`](#insn-004ffcdc) → [`004ffce8`](#insn-004ffce8)
  - `FALL_THROUGH` [`004ffcdc`](#insn-004ffcdc) → [`004ffce0`](#insn-004ffce0)
- ブロック [`004ffce0`](#insn-004ffce0) 範囲 `[['004ffce0', '004ffce7']]`
  - `FALL_THROUGH` [`004ffce4`](#insn-004ffce4) → [`004ffce8`](#insn-004ffce8)
- ブロック [`004ffce8`](#insn-004ffce8) 範囲 `[['004ffce8', '004ffd17']]`
  - `CONDITIONAL_JUMP` [`004ffd14`](#insn-004ffd14) → [`004ffd20`](#insn-004ffd20)
  - `FALL_THROUGH` [`004ffd14`](#insn-004ffd14) → [`004ffd18`](#insn-004ffd18)
- ブロック [`004ffd18`](#insn-004ffd18) 範囲 `[['004ffd18', '004ffd1f']]`
  - `FALL_THROUGH` [`004ffd1c`](#insn-004ffd1c) → [`004ffd20`](#insn-004ffd20)
- ブロック [`004ffd20`](#insn-004ffd20) 範囲 `[['004ffd20', '004ffd47']]`
  - `FALL_THROUGH` [`004ffd44`](#insn-004ffd44) → [`004ffd48`](#insn-004ffd48)
- ブロック [`004ffd48`](#insn-004ffd48) 範囲 `[['004ffd48', '004ffd4f']]`
  - `CONDITIONAL_JUMP` [`004ffd4c`](#insn-004ffd4c) → [`004ffd90`](#insn-004ffd90)
  - `FALL_THROUGH` [`004ffd4c`](#insn-004ffd4c) → [`004ffd50`](#insn-004ffd50)
- ブロック [`004ffd50`](#insn-004ffd50) 範囲 `[['004ffd50', '004ffd5b']]`
  - `CONDITIONAL_JUMP` [`004ffd58`](#insn-004ffd58) → [`004ffd50`](#insn-004ffd50)
  - `FALL_THROUGH` [`004ffd58`](#insn-004ffd58) → [`004ffd5c`](#insn-004ffd5c)
- ブロック [`004ffd5c`](#insn-004ffd5c) 範囲 `[['004ffd5c', '004ffd5f']]`
  - `UNCONDITIONAL_JUMP` [`004ffd5c`](#insn-004ffd5c) → [`004ffb5c`](#insn-004ffb5c)
- ブロック [`004ffd60`](#insn-004ffd60) 範囲 `[['004ffd60', '004ffd8f']]`
  - `CONDITIONAL_JUMP` [`004ffd8c`](#insn-004ffd8c) → [`004ffd50`](#insn-004ffd50)
  - `FALL_THROUGH` [`004ffd8c`](#insn-004ffd8c) → [`004ffd90`](#insn-004ffd90)
- ブロック [`004ffd90`](#insn-004ffd90) 範囲 `[['004ffd90', '004ffda3']]`
  - `CONDITIONAL_JUMP` [`004ffda0`](#insn-004ffda0) → [`004ffd90`](#insn-004ffd90)
  - `FALL_THROUGH` [`004ffda0`](#insn-004ffda0) → [`004ffda4`](#insn-004ffda4)
- ブロック [`004ffda4`](#insn-004ffda4) 範囲 `[['004ffda4', '004ffda7']]`
  - `UNCONDITIONAL_JUMP` [`004ffda4`](#insn-004ffda4) → [`004ffb5c`](#insn-004ffb5c)
- ブロック [`004ffda8`](#insn-004ffda8) 範囲 `[['004ffda8', '004ffdbb']]`
  - `CONDITIONAL_JUMP` [`004ffdb8`](#insn-004ffdb8) → [`004ffe1c`](#insn-004ffe1c)
  - `FALL_THROUGH` [`004ffdb8`](#insn-004ffdb8) → [`004ffdbc`](#insn-004ffdbc)
- ブロック [`004ffdbc`](#insn-004ffdbc) 範囲 `[['004ffdbc', '004ffddb']]`
- ブロック [`004ffe1c`](#insn-004ffe1c) 範囲 `[['004ffe1c', '004ffe1f']]`

## 命令位置別の参照

- [`004ffab0`](#insn-004ffab0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffab4`](#insn-004ffab4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffab8`](#insn-004ffab8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffabc`](#insn-004ffabc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffac0`](#insn-004ffac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffac4`](#insn-004ffac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffad8`](#insn-004ffad8) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffaec`](#insn-004ffaec) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffaf0`](#insn-004ffaf0) → [`00548098`](../00548/00548098.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00548098` · 推定シンボル `None` · 推定型 `None`
- [`004ffaf8`](#insn-004ffaf8) → [`004ffda8`](#insn-004ffda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb08`](#insn-004ffb08) → `00c9ac10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb20`](#insn-004ffb20) → `00c930e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`004ffb24`](#insn-004ffb24) → `00c93128`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x68)))`
- [`004ffb24`](#insn-004ffb24) → `00c93130`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`004ffb30`](#insn-004ffb30) → `00c90ae0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb30`](#insn-004ffb30) → `00c90a90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb30`](#insn-004ffb30) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb38`](#insn-004ffb38) → `00c90ab8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb38`](#insn-004ffb38) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb40`](#insn-004ffb40) → `00c9b0d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb44`](#insn-004ffb44) → `00c9abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffb4c`](#insn-004ffb4c) → `00c679f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004ffb4c`](#insn-004ffb4c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb54`](#insn-004ffb54) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004ffb54`](#insn-004ffb54) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb58`](#insn-004ffb58) → [`004ffb68`](#insn-004ffb68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb64`](#insn-004ffb64) → [`004ffda8`](#insn-004ffda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb80`](#insn-004ffb80) → [`004ffc68`](#insn-004ffc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb88`](#insn-004ffb88) → [`004ffbc4`](#insn-004ffbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffb90`](#insn-004ffb90) → [`004ffd48`](#insn-004ffd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbbc`](#insn-004ffbbc) → [`004ffd48`](#insn-004ffd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbc0`](#insn-004ffbc0) → [`004ffc04`](#insn-004ffc04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffbe4`](#insn-004ffbe4) → [`004ffc04`](#insn-004ffc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc00`](#insn-004ffc00) → [`004ffd48`](#insn-004ffd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc10`](#insn-004ffc10) → [`00c59960`](../00c59/00c59960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59960` · 推定シンボル `None` · 推定型 `None`
- [`004ffc14`](#insn-004ffc14) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc18`](#insn-004ffc18) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc38`](#insn-004ffc38) → [`00c58820`](../00c58/00c58820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58820` · 推定シンボル `None` · 推定型 `None`
- [`004ffc3c`](#insn-004ffc3c) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc40`](#insn-004ffc40) → [`004ffc4c`](#insn-004ffc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc44`](#insn-004ffc44) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc48`](#insn-004ffc48) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004ffc4c`](#insn-004ffc4c) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc50`](#insn-004ffc50) → [`004ffd48`](#insn-004ffd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc54`](#insn-004ffc54) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc58`](#insn-004ffc58) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004ffc60`](#insn-004ffc60) → [`004ffd50`](#insn-004ffd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc64`](#insn-004ffc64) → [`004ffd90`](#insn-004ffd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc7c`](#insn-004ffc7c) → [`004ffd60`](#insn-004ffd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc88`](#insn-004ffc88) → [`004ffd48`](#insn-004ffd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffc98`](#insn-004ffc98) → [`005085bc`](../00508/005085bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005085bc` · 推定シンボル `None` · 推定型 `None`
- [`004ffc9c`](#insn-004ffc9c) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffca4`](#insn-004ffca4) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffca8`](#insn-004ffca8) → `00c679f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004ffca8`](#insn-004ffca8) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcb0`](#insn-004ffcb0) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcb4`](#insn-004ffcb4) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcc0`](#insn-004ffcc0) → [`00c59990`](../00c59/00c59990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59990` · 推定シンボル `None` · 推定型 `None`
- [`004ffcc4`](#insn-004ffcc4) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcc8`](#insn-004ffcc8) → `00c679f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004ffcd4`](#insn-004ffcd4) → [`00514da4`](../00514/00514da4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00514da4` · 推定シンボル `_ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE` · 推定型 `None`
- [`004ffcd8`](#insn-004ffcd8) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcdc`](#insn-004ffcdc) → [`004ffce8`](#insn-004ffce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffce0`](#insn-004ffce0) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffce4`](#insn-004ffce4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004ffce8`](#insn-004ffce8) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcf0`](#insn-004ffcf0) → [`0053af90`](../0053a/0053af90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053af90` · 推定シンボル `None` · 推定型 `None`
- [`004ffcf4`](#insn-004ffcf4) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffcfc`](#insn-004ffcfc) → `00c90a90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffcfc`](#insn-004ffcfc) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd00`](#insn-004ffd00) → `00c90a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`004ffd04`](#insn-004ffd04) → `00c90ae0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd08`](#insn-004ffd08) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd0c`](#insn-004ffd0c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd10`](#insn-004ffd10) → `00c90ab8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd10`](#insn-004ffd10) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004ffd10`](#insn-004ffd10) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd14`](#insn-004ffd14) → [`004ffd20`](#insn-004ffd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd18`](#insn-004ffd18) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd1c`](#insn-004ffd1c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004ffd24`](#insn-004ffd24) → [`00c57fa0`](../00c57/00c57fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fa0` · 推定シンボル `None` · 推定型 `None`
- [`004ffd30`](#insn-004ffd30) → `00c9ac10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ffd34`](#insn-004ffd34) → `00c930f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`004ffd38`](#insn-004ffd38) → [`00c581c0`](../00c58/00c581c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581c0` · 推定シンボル `None` · 推定型 `None`
- [`004ffd40`](#insn-004ffd40) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`004ffd4c`](#insn-004ffd4c) → [`004ffd90`](#insn-004ffd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd58`](#insn-004ffd58) → [`004ffd50`](#insn-004ffd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd5c`](#insn-004ffd5c) → [`004ffb5c`](#insn-004ffb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd64`](#insn-004ffd64) → [`00c59900`](../00c59/00c59900.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59900` · 推定シンボル `None` · 推定型 `None`
- [`004ffd80`](#insn-004ffd80) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffd84`](#insn-004ffd84) → [`00c58820`](../00c58/00c58820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58820` · 推定シンボル `None` · 推定型 `None`
- [`004ffd8c`](#insn-004ffd8c) → [`004ffd50`](#insn-004ffd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffda0`](#insn-004ffda0) → [`004ffd90`](#insn-004ffd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffda4`](#insn-004ffda4) → [`004ffb5c`](#insn-004ffb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffda8`](#insn-004ffda8) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdb0`](#insn-004ffdb0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdb8`](#insn-004ffdb8) → [`004ffe1c`](#insn-004ffe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdbc`](#insn-004ffdbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdc0`](#insn-004ffdc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdc4`](#insn-004ffdc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdc8`](#insn-004ffdc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdcc`](#insn-004ffdcc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffdd0`](#insn-004ffdd0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ffe1c`](#insn-004ffe1c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ffab0`](#insn-004ffab0)

~~~json
{
  "source": "004ffab0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffab4`](#insn-004ffab4)

~~~json
{
  "source": "004ffab4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffab8`](#insn-004ffab8)

~~~json
{
  "source": "004ffab8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffabc`](#insn-004ffabc)

~~~json
{
  "source": "004ffabc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffac0`](#insn-004ffac0)

~~~json
{
  "source": "004ffac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffac4`](#insn-004ffac4)

~~~json
{
  "source": "004ffac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffad8`](#insn-004ffad8)

~~~json
{
  "source": "004ffad8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffaec`](#insn-004ffaec)

~~~json
{
  "source": "004ffaec",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffaf0`](#insn-004ffaf0)

~~~json
{
  "source": "004ffaf0",
  "target": "00548098",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffaf8`](#insn-004ffaf8)

~~~json
{
  "source": "004ffaf8",
  "target": "004ffda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb08`](#insn-004ffb08)

~~~json
{
  "source": "004ffb08",
  "target": "00c9ac10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb20`](#insn-004ffb20)

~~~json
{
  "source": "004ffb20",
  "target": "00c930e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c930e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb24`](#insn-004ffb24)

~~~json
{
  "source": "004ffb24",
  "target": "00c93128",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93128",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x68)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb24`](#insn-004ffb24)

~~~json
{
  "source": "004ffb24",
  "target": "00c93130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93130",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb30`](#insn-004ffb30)

~~~json
{
  "source": "004ffb30",
  "target": "00c90ae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ae0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb30`](#insn-004ffb30)

~~~json
{
  "source": "004ffb30",
  "target": "00c90a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90a90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb30`](#insn-004ffb30)

~~~json
{
  "source": "004ffb30",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb38`](#insn-004ffb38)

~~~json
{
  "source": "004ffb38",
  "target": "00c90ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ab8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb38`](#insn-004ffb38)

~~~json
{
  "source": "004ffb38",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb40`](#insn-004ffb40)

~~~json
{
  "source": "004ffb40",
  "target": "00c9b0d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b0d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb44`](#insn-004ffb44)

~~~json
{
  "source": "004ffb44",
  "target": "00c9abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffb4c`](#insn-004ffb4c)

~~~json
{
  "source": "004ffb4c",
  "target": "00c679f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c679e8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffb4c`](#insn-004ffb4c)

~~~json
{
  "source": "004ffb4c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb54`](#insn-004ffb54)

~~~json
{
  "source": "004ffb54",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffb54`](#insn-004ffb54)

~~~json
{
  "source": "004ffb54",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb58`](#insn-004ffb58)

~~~json
{
  "source": "004ffb58",
  "target": "004ffb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb64`](#insn-004ffb64)

~~~json
{
  "source": "004ffb64",
  "target": "004ffda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb80`](#insn-004ffb80)

~~~json
{
  "source": "004ffb80",
  "target": "004ffc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb88`](#insn-004ffb88)

~~~json
{
  "source": "004ffb88",
  "target": "004ffbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffb90`](#insn-004ffb90)

~~~json
{
  "source": "004ffb90",
  "target": "004ffd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbbc`](#insn-004ffbbc)

~~~json
{
  "source": "004ffbbc",
  "target": "004ffd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbc0`](#insn-004ffbc0)

~~~json
{
  "source": "004ffbc0",
  "target": "004ffc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffbe4`](#insn-004ffbe4)

~~~json
{
  "source": "004ffbe4",
  "target": "004ffc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc00`](#insn-004ffc00)

~~~json
{
  "source": "004ffc00",
  "target": "004ffd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc10`](#insn-004ffc10)

~~~json
{
  "source": "004ffc10",
  "target": "00c59960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc14`](#insn-004ffc14)

~~~json
{
  "source": "004ffc14",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc18`](#insn-004ffc18)

~~~json
{
  "source": "004ffc18",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc38`](#insn-004ffc38)

~~~json
{
  "source": "004ffc38",
  "target": "00c58820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc3c`](#insn-004ffc3c)

~~~json
{
  "source": "004ffc3c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc40`](#insn-004ffc40)

~~~json
{
  "source": "004ffc40",
  "target": "004ffc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc44`](#insn-004ffc44)

~~~json
{
  "source": "004ffc44",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc48`](#insn-004ffc48)

~~~json
{
  "source": "004ffc48",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc4c`](#insn-004ffc4c)

~~~json
{
  "source": "004ffc4c",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc50`](#insn-004ffc50)

~~~json
{
  "source": "004ffc50",
  "target": "004ffd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc54`](#insn-004ffc54)

~~~json
{
  "source": "004ffc54",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc58`](#insn-004ffc58)

~~~json
{
  "source": "004ffc58",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc60`](#insn-004ffc60)

~~~json
{
  "source": "004ffc60",
  "target": "004ffd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc64`](#insn-004ffc64)

~~~json
{
  "source": "004ffc64",
  "target": "004ffd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc7c`](#insn-004ffc7c)

~~~json
{
  "source": "004ffc7c",
  "target": "004ffd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc88`](#insn-004ffc88)

~~~json
{
  "source": "004ffc88",
  "target": "004ffd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffc98`](#insn-004ffc98)

~~~json
{
  "source": "004ffc98",
  "target": "005085bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffc9c`](#insn-004ffc9c)

~~~json
{
  "source": "004ffc9c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffca4`](#insn-004ffca4)

~~~json
{
  "source": "004ffca4",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffca8`](#insn-004ffca8)

~~~json
{
  "source": "004ffca8",
  "target": "00c679f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c679e8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffca8`](#insn-004ffca8)

~~~json
{
  "source": "004ffca8",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcb0`](#insn-004ffcb0)

~~~json
{
  "source": "004ffcb0",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcb4`](#insn-004ffcb4)

~~~json
{
  "source": "004ffcb4",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcc0`](#insn-004ffcc0)

~~~json
{
  "source": "004ffcc0",
  "target": "00c59990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffcc4`](#insn-004ffcc4)

~~~json
{
  "source": "004ffcc4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcc8`](#insn-004ffcc8)

~~~json
{
  "source": "004ffcc8",
  "target": "00c679f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c679e8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffcd4`](#insn-004ffcd4)

~~~json
{
  "source": "004ffcd4",
  "target": "00514da4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffcd8`](#insn-004ffcd8)

~~~json
{
  "source": "004ffcd8",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcdc`](#insn-004ffcdc)

~~~json
{
  "source": "004ffcdc",
  "target": "004ffce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffce0`](#insn-004ffce0)

~~~json
{
  "source": "004ffce0",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffce4`](#insn-004ffce4)

~~~json
{
  "source": "004ffce4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffce8`](#insn-004ffce8)

~~~json
{
  "source": "004ffce8",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcf0`](#insn-004ffcf0)

~~~json
{
  "source": "004ffcf0",
  "target": "0053af90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffcf4`](#insn-004ffcf4)

~~~json
{
  "source": "004ffcf4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffcfc`](#insn-004ffcfc)

~~~json
{
  "source": "004ffcfc",
  "target": "00c90a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90a90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffcfc`](#insn-004ffcfc)

~~~json
{
  "source": "004ffcfc",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd00`](#insn-004ffd00)

~~~json
{
  "source": "004ffd00",
  "target": "00c90a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "8000000000000000",
  "capture_start": "00c90a78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ffd04`](#insn-004ffd04)

~~~json
{
  "source": "004ffd04",
  "target": "00c90ae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ae0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd08`](#insn-004ffd08)

~~~json
{
  "source": "004ffd08",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd0c`](#insn-004ffd0c)

~~~json
{
  "source": "004ffd0c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd10`](#insn-004ffd10)

~~~json
{
  "source": "004ffd10",
  "target": "00c90ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ab8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd10`](#insn-004ffd10)

~~~json
{
  "source": "004ffd10",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004ffd10`](#insn-004ffd10)

~~~json
{
  "source": "004ffd10",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd14`](#insn-004ffd14)

~~~json
{
  "source": "004ffd14",
  "target": "004ffd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd18`](#insn-004ffd18)

~~~json
{
  "source": "004ffd18",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd1c`](#insn-004ffd1c)

~~~json
{
  "source": "004ffd1c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd24`](#insn-004ffd24)

~~~json
{
  "source": "004ffd24",
  "target": "00c57fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd30`](#insn-004ffd30)

~~~json
{
  "source": "004ffd30",
  "target": "00c9ac10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd34`](#insn-004ffd34)

~~~json
{
  "source": "004ffd34",
  "target": "00c930f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c930f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ffd38`](#insn-004ffd38)

~~~json
{
  "source": "004ffd38",
  "target": "00c581c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd40`](#insn-004ffd40)

~~~json
{
  "source": "004ffd40",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd4c`](#insn-004ffd4c)

~~~json
{
  "source": "004ffd4c",
  "target": "004ffd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd58`](#insn-004ffd58)

~~~json
{
  "source": "004ffd58",
  "target": "004ffd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd5c`](#insn-004ffd5c)

~~~json
{
  "source": "004ffd5c",
  "target": "004ffb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd64`](#insn-004ffd64)

~~~json
{
  "source": "004ffd64",
  "target": "00c59900",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd80`](#insn-004ffd80)

~~~json
{
  "source": "004ffd80",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffd84`](#insn-004ffd84)

~~~json
{
  "source": "004ffd84",
  "target": "00c58820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ffd8c`](#insn-004ffd8c)

~~~json
{
  "source": "004ffd8c",
  "target": "004ffd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffda0`](#insn-004ffda0)

~~~json
{
  "source": "004ffda0",
  "target": "004ffd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffda4`](#insn-004ffda4)

~~~json
{
  "source": "004ffda4",
  "target": "004ffb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffda8`](#insn-004ffda8)

~~~json
{
  "source": "004ffda8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdb0`](#insn-004ffdb0)

~~~json
{
  "source": "004ffdb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdb8`](#insn-004ffdb8)

~~~json
{
  "source": "004ffdb8",
  "target": "004ffe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdbc`](#insn-004ffdbc)

~~~json
{
  "source": "004ffdbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdc0`](#insn-004ffdc0)

~~~json
{
  "source": "004ffdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdc4`](#insn-004ffdc4)

~~~json
{
  "source": "004ffdc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdc8`](#insn-004ffdc8)

~~~json
{
  "source": "004ffdc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdcc`](#insn-004ffdcc)

~~~json
{
  "source": "004ffdcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffdd0`](#insn-004ffdd0)

~~~json
{
  "source": "004ffdd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ffe1c`](#insn-004ffe1c)

~~~json
{
  "source": "004ffe1c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
