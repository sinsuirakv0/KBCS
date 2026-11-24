# 00ac8bec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac7bf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac7/00ac7bf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-180eee184be75e6d747f9529b97e2422)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8bec",
  "name": "FUN_00ac8bec",
  "size": 1020,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bf4480b4598c92487e3d37d65ea235c74989e902f5c038f46cc13877f18625b",
  "source_text_sha256": "0bf4480b4598c92487e3d37d65ea235c74989e902f5c038f46cc13877f18625b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac8bec",
        "00ac8fe7"
      ]
    ],
    "bytes_sha256": "35707de1bea6747d700e64c111067d0ed189e25bb306c4e0a150f9c427cacfbd",
    "instruction_count": 255,
    "instruction_bytes": 1020,
    "body_bytes": 1020,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [0078a084](../0078a/0078a084.md)
- [0083012c](../00830/0083012c.md)
- [008cc434](../008cc/008cc434.md)
- [008d41f8](../008d4/008d41f8.md)
- [008ffd30](../008ff/008ffd30.md)
- [00a3f25c](../00a3f/00a3f25c.md)
- [00a76e10](../00a76/00a76e10.md)
- [00ac1960](../00ac1/00ac1960.md)

## 呼び出し先

- [0045a0d4](../0045a/0045a0d4.md)
- [0046cd24](../0046c/0046cd24.md)
- [008524fc](../00852/008524fc.md)
- [00ac9044](../00ac9/00ac9044.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6342 bytes

~~~c

undefined8 FUN_00ac8bec(int *param_1)

{
  uint uVar1;
  char cVar2;
  undefined4 uVar3;
  long lVar4;
  long *plVar5;
  int iVar6;
  
  if (*param_1 != 0x7fffffff) {
    *param_1 = *param_1 + 1;
  }
  if ((char)param_1[0x28] != '\0') {
    iVar6 = param_1[0x29];
    param_1[0x29] = iVar6 + 1;
    if (iVar6 < 0x18) {
      return 1;
    }
    if (*(long **)(param_1 + 0x58) != (long *)0x0) {
      (**(code **)(**(long **)(param_1 + 0x58) + 0x30))();
      *(undefined1 *)(param_1 + 0x28) = 0;
      return 0;
    }
LAB_00ac8fe4:
                    /* WARNING: Subroutine does not return */
    FUN_0045a0d4();
  }
  lVar4 = FUN_008524fc();
  cVar2 = *(char *)((long)&fde_table_entry_00332a20.data_loc + lVar4);
  lVar4 = FUN_008524fc();
  if (cVar2 == '\0') {
    if (*(char *)((long)&fde_table_entry_00332a20.data_loc + lVar4 + 1) != '\0') {
      lVar4 = FUN_008524fc();
      cVar2 = *(char *)((long)param_1 + 0x1b9);
      *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) =
           *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) + 1;
      if (cVar2 != '\0') {
        lVar4 = FUN_008524fc();
        iVar6 = *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4);
        lVar4 = FUN_008524fc();
        *(uint *)((long)&fde_table_entry_00334170.data_loc + lVar4) = iVar6 << 1 | 1;
        lVar4 = FUN_008524fc();
        iVar6 = *(int *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4);
        lVar4 = FUN_008524fc();
        *(uint *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4) = iVar6 << 1 | 1;
      }
      lVar4 = FUN_008524fc();
      if (0x128 < *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4)) {
        lVar4 = FUN_008524fc();
        *(undefined4 *)((long)&fde_table_entry_00334170.data_loc + lVar4) = 0x129;
        lVar4 = FUN_008524fc();
        *(undefined4 *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4) = 0x7e;
        lVar4 = FUN_008524fc();
        iVar6 = *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4);
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        lVar4 = FUN_008524fc();
        *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4) = iVar6 >> 1;
      }
      lVar4 = FUN_008524fc();
      uVar1 = *(uint *)((long)&fde_table_entry_00333f90.initial_loc + lVar4);
      FUN_008524fc();
      FUN_008524fc();
      lVar4 = FUN_008524fc();
      if (uVar1 < 0xc) {
        lVar4 = FUN_008524fc();
        uVar3 = *(undefined4 *)
                 (PTR_DAT_00c9c5d0 +
                 (long)(int)~*(uint *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) * 4 +
                 0x30);
        goto LAB_00ac8f6c;
      }
      *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0xb;
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00333f80.data_loc + lVar4) = 0;
      lVar4 = FUN_008524fc();
      if ((*(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4) < 1) ||
         (*(char *)((long)param_1 + 0x1b9) == '\0')) {
        lVar4 = FUN_008524fc();
        *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar4 + 1) = 0;
        lVar4 = FUN_008524fc();
        plVar5 = *(long **)(param_1 + 0x40);
        *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0;
        if (plVar5 != (long *)0x0) {
          (**(code **)(*plVar5 + 0x30))();
          return 0;
        }
        goto LAB_00ac8fe4;
      }
    }
  }
  else {
    iVar6 = param_1[0x6e];
    *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) =
         *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) + 1;
    if ((char)iVar6 != '\0') {
      lVar4 = FUN_008524fc();
      iVar6 = *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4);
      lVar4 = FUN_008524fc();
      *(uint *)((long)&fde_table_entry_00334170.initial_loc + lVar4) = iVar6 << 1 | 1;
    }
    lVar4 = FUN_008524fc();
    if (0x128 < *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4)) {
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00334170.initial_loc + lVar4) = 0x129;
      lVar4 = FUN_008524fc();
      iVar6 = *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4);
      if (iVar6 < 0) {
        iVar6 = iVar6 + 1;
      }
      lVar4 = FUN_008524fc();
      *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4) = iVar6 >> 1;
      lVar4 = FUN_008524fc();
      iVar6 = *(int *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4);
      if (iVar6 < 0) {
        iVar6 = iVar6 + 1;
      }
      lVar4 = FUN_008524fc();
      *(int *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4) = iVar6 >> 1;
    }
    lVar4 = FUN_008524fc();
    uVar1 = *(uint *)((long)&fde_table_entry_00333f90.initial_loc + lVar4);
    FUN_008524fc();
    FUN_008524fc();
    lVar4 = FUN_008524fc();
    if (uVar1 < 0xc) {
      uVar3 = *(undefined4 *)
               (PTR_DAT_00c9c5d0 +
               (long)*(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) * 4);
LAB_00ac8f6c:
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00333f80.data_loc + lVar4) = uVar3;
    }
    else {
      *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0xb;
      FUN_008524fc();
      uVar3 = FUN_0046cd24();
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00333f80.data_loc + lVar4) = uVar3;
      lVar4 = FUN_008524fc();
      if ((*(int *)((long)&fde_table_entry_00334170.data_loc + lVar4) < 1) ||
         ((char)param_1[0x6e] == '\0')) {
        lVar4 = FUN_008524fc();
        *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar4) = 0;
        lVar4 = FUN_008524fc();
        plVar5 = *(long **)(param_1 + 0x4c);
        *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0;
        if (plVar5 == (long *)0x0) goto LAB_00ac8fe4;
        (**(code **)(*plVar5 + 0x30))();
      }
    }
  }
  if (param_1[0x27] == 1) {
    iVar6 = param_1[0x26];
    param_1[0x26] = iVar6 + 1U;
    FUN_008524fc();
    if (iVar6 + 1U < 0x10) goto LAB_00ac8fc8;
    iVar6 = 0;
  }
  else {
    if ((param_1[0x27] != 2) || (iVar6 = param_1[0x26], param_1[0x26] = iVar6 + -1, 0 < iVar6))
    goto LAB_00ac8fc8;
    iVar6 = 3;
  }
  param_1[0x27] = iVar6;
LAB_00ac8fc8:
  FUN_00ac9044(param_1);
  return 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac8bec"></a> `00ac8bec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ac8bf0"></a> `00ac8bf0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac8bf4"></a> `00ac8bf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac8bf8"></a> `00ac8bf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac8bfc"></a> `00ac8bfc` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-00ac8c00"></a> `00ac8c00` | `09 00 b0 12` | mov w9,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00ac8c04"></a> `00ac8c04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac8c08"></a> `00ac8c08` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00ac8c0c"></a> `00ac8c0c` | `60 00 00 54` | b.eq 0x00ac8c18 | `CONDITIONAL_JUMP`
<a id="insn-00ac8c10"></a> `00ac8c10` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8c14"></a> `00ac8c14` | `68 02 00 b9` | str w8,[x19] | `FALL_THROUGH`
<a id="insn-00ac8c18"></a> `00ac8c18` | `68 82 42 39` | ldrb w8,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00ac8c1c"></a> `00ac8c1c` | `c8 01 00 34` | cbz w8,0x00ac8c54 | `CONDITIONAL_JUMP`
<a id="insn-00ac8c20"></a> `00ac8c20` | `68 a6 40 b9` | ldr w8,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00ac8c24"></a> `00ac8c24` | `09 05 00 11` | add w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8c28"></a> `00ac8c28` | `1f 61 00 71` | cmp w8,#0x18 | `FALL_THROUGH`
<a id="insn-00ac8c2c"></a> `00ac8c2c` | `69 a6 00 b9` | str w9,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00ac8c30"></a> `00ac8c30` | `0b 1d 00 54` | b.lt 0x00ac8fd0 | `CONDITIONAL_JUMP`
<a id="insn-00ac8c34"></a> `00ac8c34` | `60 b2 40 f9` | ldr x0,[x19, #0x160] | `FALL_THROUGH`
<a id="insn-00ac8c38"></a> `00ac8c38` | `60 1d 00 b4` | cbz x0,0x00ac8fe4 | `CONDITIONAL_JUMP`
<a id="insn-00ac8c3c"></a> `00ac8c3c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac8c40"></a> `00ac8c40` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ac8c44"></a> `00ac8c44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac8c48"></a> `00ac8c48` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ac8c4c"></a> `00ac8c4c` | `7f 82 02 39` | strb wzr,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00ac8c50"></a> `00ac8c50` | `e1 00 00 14` | b 0x00ac8fd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8c54"></a> `00ac8c54` | `2a 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8c58"></a> `00ac8c58` | `88 44 85 52` | mov w8,#0x2a24 | `FALL_THROUGH`
<a id="insn-00ac8c5c"></a> `00ac8c5c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8c60"></a> `00ac8c60` | `14 68 68 38` | ldrb w20,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac8c64"></a> `00ac8c64` | `26 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8c68"></a> `00ac8c68` | `d4 0a 00 34` | cbz w20,0x00ac8dc0 | `CONDITIONAL_JUMP`
<a id="insn-00ac8c6c"></a> `00ac8c6c` | `08 f2 87 52` | mov w8,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8c70"></a> `00ac8c70` | `6a e2 46 39` | ldrb w10,[x19, #0x1b8] | `FALL_THROUGH`
<a id="insn-00ac8c74"></a> `00ac8c74` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8c78"></a> `00ac8c78` | `09 68 68 b8` | ldr w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8c7c"></a> `00ac8c7c` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8c80"></a> `00ac8c80` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8c84"></a> `00ac8c84` | `2a 01 00 34` | cbz w10,0x00ac8ca8 | `CONDITIONAL_JUMP`
<a id="insn-00ac8c88"></a> `00ac8c88` | `1d 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8c8c"></a> `00ac8c8c` | `14 2e 88 52` | mov w20,#0x4170 | `FALL_THROUGH`
<a id="insn-00ac8c90"></a> `00ac8c90` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8c94"></a> `00ac8c94` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8c98"></a> `00ac8c98` | `08 68 74 b8` | ldr w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8c9c"></a> `00ac8c9c` | `35 05 08 2a` | orr w21,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00ac8ca0"></a> `00ac8ca0` | `17 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ca4"></a> `00ac8ca4` | `15 68 34 b8` | str w21,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8ca8"></a> `00ac8ca8` | `15 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8cac"></a> `00ac8cac` | `08 2e 88 52` | mov w8,#0x4170 | `FALL_THROUGH`
<a id="insn-00ac8cb0"></a> `00ac8cb0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8cb4"></a> `00ac8cb4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8cb8"></a> `00ac8cb8` | `1f a5 04 71` | cmp w8,#0x129 | `FALL_THROUGH`
<a id="insn-00ac8cbc"></a> `00ac8cbc` | `0b 03 00 54` | b.lt 0x00ac8d1c | `CONDITIONAL_JUMP`
<a id="insn-00ac8cc0"></a> `00ac8cc0` | `0f 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8cc4"></a> `00ac8cc4` | `08 2e 88 52` | mov w8,#0x4170 | `FALL_THROUGH`
<a id="insn-00ac8cc8"></a> `00ac8cc8` | `29 25 80 52` | mov w9,#0x129 | `FALL_THROUGH`
<a id="insn-00ac8ccc"></a> `00ac8ccc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8cd0"></a> `00ac8cd0` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8cd4"></a> `00ac8cd4` | `0a 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8cd8"></a> `00ac8cd8` | `94 2e 88 52` | mov w20,#0x4174 | `FALL_THROUGH`
<a id="insn-00ac8cdc"></a> `00ac8cdc` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8ce0"></a> `00ac8ce0` | `08 68 74 b8` | ldr w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8ce4"></a> `00ac8ce4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00ac8ce8"></a> `00ac8ce8` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00ac8cec"></a> `00ac8cec` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8cf0"></a> `00ac8cf0` | `03 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8cf4"></a> `00ac8cf4` | `15 68 34 b8` | str w21,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8cf8"></a> `00ac8cf8` | `01 26 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8cfc"></a> `00ac8cfc` | `14 f4 87 52` | mov w20,#0x3fa0 | `FALL_THROUGH`
<a id="insn-00ac8d00"></a> `00ac8d00` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8d04"></a> `00ac8d04` | `08 68 74 b8` | ldr w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8d08"></a> `00ac8d08` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00ac8d0c"></a> `00ac8d0c` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00ac8d10"></a> `00ac8d10` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8d14"></a> `00ac8d14` | `fa 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d18"></a> `00ac8d18` | `15 68 34 b8` | str w21,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8d1c"></a> `00ac8d1c` | `f8 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d20"></a> `00ac8d20` | `14 f2 87 52` | mov w20,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8d24"></a> `00ac8d24` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8d28"></a> `00ac8d28` | `15 68 74 b8` | ldr w21,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8d2c"></a> `00ac8d2c` | `f4 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d30"></a> `00ac8d30` | `f3 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d34"></a> `00ac8d34` | `f2 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d38"></a> `00ac8d38` | `bf 32 00 71` | cmp w21,#0xc | `FALL_THROUGH`
<a id="insn-00ac8d3c"></a> `00ac8d3c` | `c3 0f 00 54` | b.cc 0x00ac8f34 | `CONDITIONAL_JUMP`
<a id="insn-00ac8d40"></a> `00ac8d40` | `68 01 80 52` | mov w8,#0xb | `FALL_THROUGH`
<a id="insn-00ac8d44"></a> `00ac8d44` | `08 68 34 b8` | str w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8d48"></a> `00ac8d48` | `ed 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d4c"></a> `00ac8d4c` | `f6 8f e6 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d50"></a> `00ac8d50` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ac8d54"></a> `00ac8d54` | `ea 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d58"></a> `00ac8d58` | `88 f0 87 52` | mov w8,#0x3f84 | `FALL_THROUGH`
<a id="insn-00ac8d5c"></a> `00ac8d5c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8d60"></a> `00ac8d60` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8d64"></a> `00ac8d64` | `e6 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d68"></a> `00ac8d68` | `88 2e 88 52` | mov w8,#0x4174 | `FALL_THROUGH`
<a id="insn-00ac8d6c"></a> `00ac8d6c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8d70"></a> `00ac8d70` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8d74"></a> `00ac8d74` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8d78"></a> `00ac8d78` | `6b 00 00 54` | b.lt 0x00ac8d84 | `CONDITIONAL_JUMP`
<a id="insn-00ac8d7c"></a> `00ac8d7c` | `68 e2 46 39` | ldrb w8,[x19, #0x1b8] | `FALL_THROUGH`
<a id="insn-00ac8d80"></a> `00ac8d80` | `e8 0f 00 35` | cbnz w8,0x00ac8f7c | `CONDITIONAL_JUMP`
<a id="insn-00ac8d84"></a> `00ac8d84` | `de 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d88"></a> `00ac8d88` | `88 44 85 52` | mov w8,#0x2a24 | `FALL_THROUGH`
<a id="insn-00ac8d8c"></a> `00ac8d8c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8d90"></a> `00ac8d90` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac8d94"></a> `00ac8d94` | `da 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8d98"></a> `00ac8d98` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ac8d9c"></a> `00ac8d9c` | `60 9a 40 f9` | ldr x0,[x19, #0x130] | `FALL_THROUGH`
<a id="insn-00ac8da0"></a> `00ac8da0` | `09 f2 87 52` | mov w9,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8da4"></a> `00ac8da4` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8da8"></a> `00ac8da8` | `1f 69 29 b8` | str wzr,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8dac"></a> `00ac8dac` | `c0 11 00 b4` | cbz x0,0x00ac8fe4 | `CONDITIONAL_JUMP`
<a id="insn-00ac8db0"></a> `00ac8db0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac8db4"></a> `00ac8db4` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ac8db8"></a> `00ac8db8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac8dbc"></a> `00ac8dbc` | `70 00 00 14` | b 0x00ac8f7c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8dc0"></a> `00ac8dc0` | `a8 44 85 52` | mov w8,#0x2a25 | `FALL_THROUGH`
<a id="insn-00ac8dc4"></a> `00ac8dc4` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8dc8"></a> `00ac8dc8` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac8dcc"></a> `00ac8dcc` | `88 0d 00 34` | cbz w8,0x00ac8f7c | `CONDITIONAL_JUMP`
<a id="insn-00ac8dd0"></a> `00ac8dd0` | `cb 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8dd4"></a> `00ac8dd4` | `08 f2 87 52` | mov w8,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8dd8"></a> `00ac8dd8` | `6a e6 46 39` | ldrb w10,[x19, #0x1b9] | `FALL_THROUGH`
<a id="insn-00ac8ddc"></a> `00ac8ddc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8de0"></a> `00ac8de0` | `09 68 68 b8` | ldr w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8de4"></a> `00ac8de4` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8de8"></a> `00ac8de8` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8dec"></a> `00ac8dec` | `0a 02 00 34` | cbz w10,0x00ac8e2c | `CONDITIONAL_JUMP`
<a id="insn-00ac8df0"></a> `00ac8df0` | `c3 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8df4"></a> `00ac8df4` | `94 2e 88 52` | mov w20,#0x4174 | `FALL_THROUGH`
<a id="insn-00ac8df8"></a> `00ac8df8` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8dfc"></a> `00ac8dfc` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e00"></a> `00ac8e00` | `08 68 74 b8` | ldr w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e04"></a> `00ac8e04` | `b6 06 08 2a` | orr w22,w21,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00ac8e08"></a> `00ac8e08` | `bd 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e0c"></a> `00ac8e0c` | `16 68 34 b8` | str w22,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e10"></a> `00ac8e10` | `bb 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e14"></a> `00ac8e14` | `14 f4 87 52` | mov w20,#0x3fa0 | `FALL_THROUGH`
<a id="insn-00ac8e18"></a> `00ac8e18` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e1c"></a> `00ac8e1c` | `08 68 74 b8` | ldr w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e20"></a> `00ac8e20` | `b5 06 08 2a` | orr w21,w21,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00ac8e24"></a> `00ac8e24` | `b6 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e28"></a> `00ac8e28` | `15 68 34 b8` | str w21,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e2c"></a> `00ac8e2c` | `b4 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e30"></a> `00ac8e30` | `88 2e 88 52` | mov w8,#0x4174 | `FALL_THROUGH`
<a id="insn-00ac8e34"></a> `00ac8e34` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e38"></a> `00ac8e38` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e3c"></a> `00ac8e3c` | `1f a5 04 71` | cmp w8,#0x129 | `FALL_THROUGH`
<a id="insn-00ac8e40"></a> `00ac8e40` | `8b 02 00 54` | b.lt 0x00ac8e90 | `CONDITIONAL_JUMP`
<a id="insn-00ac8e44"></a> `00ac8e44` | `ae 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e48"></a> `00ac8e48` | `88 2e 88 52` | mov w8,#0x4174 | `FALL_THROUGH`
<a id="insn-00ac8e4c"></a> `00ac8e4c` | `29 25 80 52` | mov w9,#0x129 | `FALL_THROUGH`
<a id="insn-00ac8e50"></a> `00ac8e50` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e54"></a> `00ac8e54` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e58"></a> `00ac8e58` | `a9 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e5c"></a> `00ac8e5c` | `08 f4 87 52` | mov w8,#0x3fa0 | `FALL_THROUGH`
<a id="insn-00ac8e60"></a> `00ac8e60` | `c9 0f 80 52` | mov w9,#0x7e | `FALL_THROUGH`
<a id="insn-00ac8e64"></a> `00ac8e64` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e68"></a> `00ac8e68` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e6c"></a> `00ac8e6c` | `a4 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e70"></a> `00ac8e70` | `14 2e 88 52` | mov w20,#0x4170 | `FALL_THROUGH`
<a id="insn-00ac8e74"></a> `00ac8e74` | `74 06 a0 72` | movk w20,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e78"></a> `00ac8e78` | `08 68 74 b8` | ldr w8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e7c"></a> `00ac8e7c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00ac8e80"></a> `00ac8e80` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00ac8e84"></a> `00ac8e84` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8e88"></a> `00ac8e88` | `9d 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e8c"></a> `00ac8e8c` | `15 68 34 b8` | str w21,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8e90"></a> `00ac8e90` | `9b 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8e94"></a> `00ac8e94` | `08 f2 87 52` | mov w8,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8e98"></a> `00ac8e98` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8e9c"></a> `00ac8e9c` | `14 68 68 b8` | ldr w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8ea0"></a> `00ac8ea0` | `97 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ea4"></a> `00ac8ea4` | `96 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ea8"></a> `00ac8ea8` | `95 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8eac"></a> `00ac8eac` | `9f 32 00 71` | cmp w20,#0xc | `FALL_THROUGH`
<a id="insn-00ac8eb0"></a> `00ac8eb0` | `c3 04 00 54` | b.cc 0x00ac8f48 | `CONDITIONAL_JUMP`
<a id="insn-00ac8eb4"></a> `00ac8eb4` | `08 f2 87 52` | mov w8,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8eb8"></a> `00ac8eb8` | `69 01 80 52` | mov w9,#0xb | `FALL_THROUGH`
<a id="insn-00ac8ebc"></a> `00ac8ebc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8ec0"></a> `00ac8ec0` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8ec4"></a> `00ac8ec4` | `8e 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ec8"></a> `00ac8ec8` | `88 f0 87 52` | mov w8,#0x3f84 | `FALL_THROUGH`
<a id="insn-00ac8ecc"></a> `00ac8ecc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8ed0"></a> `00ac8ed0` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8ed4"></a> `00ac8ed4` | `8a 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ed8"></a> `00ac8ed8` | `08 2e 88 52` | mov w8,#0x4170 | `FALL_THROUGH`
<a id="insn-00ac8edc"></a> `00ac8edc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8ee0"></a> `00ac8ee0` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8ee4"></a> `00ac8ee4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8ee8"></a> `00ac8ee8` | `6b 00 00 54` | b.lt 0x00ac8ef4 | `CONDITIONAL_JUMP`
<a id="insn-00ac8eec"></a> `00ac8eec` | `68 e6 46 39` | ldrb w8,[x19, #0x1b9] | `FALL_THROUGH`
<a id="insn-00ac8ef0"></a> `00ac8ef0` | `68 04 00 35` | cbnz w8,0x00ac8f7c | `CONDITIONAL_JUMP`
<a id="insn-00ac8ef4"></a> `00ac8ef4` | `82 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ef8"></a> `00ac8ef8` | `a8 44 85 52` | mov w8,#0x2a25 | `FALL_THROUGH`
<a id="insn-00ac8efc"></a> `00ac8efc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8f00"></a> `00ac8f00` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac8f04"></a> `00ac8f04` | `7e 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f08"></a> `00ac8f08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ac8f0c"></a> `00ac8f0c` | `60 82 40 f9` | ldr x0,[x19, #0x100] | `FALL_THROUGH`
<a id="insn-00ac8f10"></a> `00ac8f10` | `09 f2 87 52` | mov w9,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8f14"></a> `00ac8f14` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8f18"></a> `00ac8f18` | `1f 69 29 b8` | str wzr,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8f1c"></a> `00ac8f1c` | `40 06 00 b4` | cbz x0,0x00ac8fe4 | `CONDITIONAL_JUMP`
<a id="insn-00ac8f20"></a> `00ac8f20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac8f24"></a> `00ac8f24` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ac8f28"></a> `00ac8f28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac8f2c"></a> `00ac8f2c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ac8f30"></a> `00ac8f30` | `29 00 00 14` | b 0x00ac8fd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8f34"></a> `00ac8f34` | `a9 0e 00 90` | adrp x9,0xc9c000 | `FALL_THROUGH`
<a id="insn-00ac8f38"></a> `00ac8f38` | `08 68 b4 b8` | ldrsw x8,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8f3c"></a> `00ac8f3c` | `29 e9 42 f9` | ldr x9,[x9, #0x5d0] | `FALL_THROUGH`
<a id="insn-00ac8f40"></a> `00ac8f40` | `34 79 68 b8` | ldr w20,[x9, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ac8f44"></a> `00ac8f44` | `0a 00 00 14` | b 0x00ac8f6c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8f48"></a> `00ac8f48` | `6d 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f4c"></a> `00ac8f4c` | `08 f2 87 52` | mov w8,#0x3f90 | `FALL_THROUGH`
<a id="insn-00ac8f50"></a> `00ac8f50` | `a9 0e 00 90` | adrp x9,0xc9c000 | `FALL_THROUGH`
<a id="insn-00ac8f54"></a> `00ac8f54` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8f58"></a> `00ac8f58` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8f5c"></a> `00ac8f5c` | `29 e9 42 f9` | ldr x9,[x9, #0x5d0] | `FALL_THROUGH`
<a id="insn-00ac8f60"></a> `00ac8f60` | `e8 03 28 2a` | mvn w8,w8 | `FALL_THROUGH`
<a id="insn-00ac8f64"></a> `00ac8f64` | `28 c9 28 8b` | add x8,x9,w8, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00ac8f68"></a> `00ac8f68` | `14 31 40 b9` | ldr w20,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ac8f6c"></a> `00ac8f6c` | `64 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f70"></a> `00ac8f70` | `88 f0 87 52` | mov w8,#0x3f84 | `FALL_THROUGH`
<a id="insn-00ac8f74"></a> `00ac8f74` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac8f78"></a> `00ac8f78` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac8f7c"></a> `00ac8f7c` | `68 9e 40 b9` | ldr w8,[x19, #0x9c] | `FALL_THROUGH`
<a id="insn-00ac8f80"></a> `00ac8f80` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8f84"></a> `00ac8f84` | `20 01 00 54` | b.eq 0x00ac8fa8 | `CONDITIONAL_JUMP`
<a id="insn-00ac8f88"></a> `00ac8f88` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00ac8f8c"></a> `00ac8f8c` | `e1 01 00 54` | b.ne 0x00ac8fc8 | `CONDITIONAL_JUMP`
<a id="insn-00ac8f90"></a> `00ac8f90` | `68 9a 40 b9` | ldr w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00ac8f94"></a> `00ac8f94` | `08 05 00 71` | subs w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8f98"></a> `00ac8f98` | `68 9a 00 b9` | str w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00ac8f9c"></a> `00ac8f9c` | `6a 01 00 54` | b.ge 0x00ac8fc8 | `CONDITIONAL_JUMP`
<a id="insn-00ac8fa0"></a> `00ac8fa0` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00ac8fa4"></a> `00ac8fa4` | `08 00 00 14` | b 0x00ac8fc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8fa8"></a> `00ac8fa8` | `68 9a 40 b9` | ldr w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00ac8fac"></a> `00ac8fac` | `14 05 00 11` | add w20,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8fb0"></a> `00ac8fb0` | `74 9a 00 b9` | str w20,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00ac8fb4"></a> `00ac8fb4` | `52 25 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8fb8"></a> `00ac8fb8` | `9f 42 00 71` | cmp w20,#0x10 | `FALL_THROUGH`
<a id="insn-00ac8fbc"></a> `00ac8fbc` | `63 00 00 54` | b.cc 0x00ac8fc8 | `CONDITIONAL_JUMP`
<a id="insn-00ac8fc0"></a> `00ac8fc0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00ac8fc4"></a> `00ac8fc4` | `68 9e 00 b9` | str w8,[x19, #0x9c] | `FALL_THROUGH`
<a id="insn-00ac8fc8"></a> `00ac8fc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac8fcc"></a> `00ac8fcc` | `1e 00 00 94` | bl 0x00ac9044 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8fd0"></a> `00ac8fd0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8fd4"></a> `00ac8fd4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac8fd8"></a> `00ac8fd8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac8fdc"></a> `00ac8fdc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ac8fe0"></a> `00ac8fe0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac8fe4"></a> `00ac8fe4` | `3c 44 e6 97` | bl 0x0045a0d4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac8bec`](#insn-00ac8bec) 範囲 `[['00ac8bec', '00ac8c0f']]`
  - `CONDITIONAL_JUMP` [`00ac8c0c`](#insn-00ac8c0c) → [`00ac8c18`](#insn-00ac8c18)
  - `FALL_THROUGH` [`00ac8c0c`](#insn-00ac8c0c) → [`00ac8c10`](#insn-00ac8c10)
- ブロック [`00ac8c10`](#insn-00ac8c10) 範囲 `[['00ac8c10', '00ac8c17']]`
  - `FALL_THROUGH` [`00ac8c14`](#insn-00ac8c14) → [`00ac8c18`](#insn-00ac8c18)
- ブロック [`00ac8c18`](#insn-00ac8c18) 範囲 `[['00ac8c18', '00ac8c1f']]`
  - `CONDITIONAL_JUMP` [`00ac8c1c`](#insn-00ac8c1c) → [`00ac8c54`](#insn-00ac8c54)
  - `FALL_THROUGH` [`00ac8c1c`](#insn-00ac8c1c) → [`00ac8c20`](#insn-00ac8c20)
- ブロック [`00ac8c20`](#insn-00ac8c20) 範囲 `[['00ac8c20', '00ac8c33']]`
  - `CONDITIONAL_JUMP` [`00ac8c30`](#insn-00ac8c30) → [`00ac8fd0`](#insn-00ac8fd0)
  - `FALL_THROUGH` [`00ac8c30`](#insn-00ac8c30) → [`00ac8c34`](#insn-00ac8c34)
- ブロック [`00ac8c34`](#insn-00ac8c34) 範囲 `[['00ac8c34', '00ac8c3b']]`
  - `CONDITIONAL_JUMP` [`00ac8c38`](#insn-00ac8c38) → [`00ac8fe4`](#insn-00ac8fe4)
  - `FALL_THROUGH` [`00ac8c38`](#insn-00ac8c38) → [`00ac8c3c`](#insn-00ac8c3c)
- ブロック [`00ac8c3c`](#insn-00ac8c3c) 範囲 `[['00ac8c3c', '00ac8c53']]`
  - `UNCONDITIONAL_JUMP` [`00ac8c50`](#insn-00ac8c50) → [`00ac8fd4`](#insn-00ac8fd4)
- ブロック [`00ac8c54`](#insn-00ac8c54) 範囲 `[['00ac8c54', '00ac8c6b']]`
  - `CONDITIONAL_JUMP` [`00ac8c68`](#insn-00ac8c68) → [`00ac8dc0`](#insn-00ac8dc0)
  - `FALL_THROUGH` [`00ac8c68`](#insn-00ac8c68) → [`00ac8c6c`](#insn-00ac8c6c)
- ブロック [`00ac8c6c`](#insn-00ac8c6c) 範囲 `[['00ac8c6c', '00ac8c87']]`
  - `CONDITIONAL_JUMP` [`00ac8c84`](#insn-00ac8c84) → [`00ac8ca8`](#insn-00ac8ca8)
  - `FALL_THROUGH` [`00ac8c84`](#insn-00ac8c84) → [`00ac8c88`](#insn-00ac8c88)
- ブロック [`00ac8c88`](#insn-00ac8c88) 範囲 `[['00ac8c88', '00ac8ca7']]`
  - `FALL_THROUGH` [`00ac8ca4`](#insn-00ac8ca4) → [`00ac8ca8`](#insn-00ac8ca8)
- ブロック [`00ac8ca8`](#insn-00ac8ca8) 範囲 `[['00ac8ca8', '00ac8cbf']]`
  - `CONDITIONAL_JUMP` [`00ac8cbc`](#insn-00ac8cbc) → [`00ac8d1c`](#insn-00ac8d1c)
  - `FALL_THROUGH` [`00ac8cbc`](#insn-00ac8cbc) → [`00ac8cc0`](#insn-00ac8cc0)
- ブロック [`00ac8cc0`](#insn-00ac8cc0) 範囲 `[['00ac8cc0', '00ac8d1b']]`
  - `FALL_THROUGH` [`00ac8d18`](#insn-00ac8d18) → [`00ac8d1c`](#insn-00ac8d1c)
- ブロック [`00ac8d1c`](#insn-00ac8d1c) 範囲 `[['00ac8d1c', '00ac8d3f']]`
  - `CONDITIONAL_JUMP` [`00ac8d3c`](#insn-00ac8d3c) → [`00ac8f34`](#insn-00ac8f34)
  - `FALL_THROUGH` [`00ac8d3c`](#insn-00ac8d3c) → [`00ac8d40`](#insn-00ac8d40)
- ブロック [`00ac8d40`](#insn-00ac8d40) 範囲 `[['00ac8d40', '00ac8d7b']]`
  - `CONDITIONAL_JUMP` [`00ac8d78`](#insn-00ac8d78) → [`00ac8d84`](#insn-00ac8d84)
  - `FALL_THROUGH` [`00ac8d78`](#insn-00ac8d78) → [`00ac8d7c`](#insn-00ac8d7c)
- ブロック [`00ac8d7c`](#insn-00ac8d7c) 範囲 `[['00ac8d7c', '00ac8d83']]`
  - `CONDITIONAL_JUMP` [`00ac8d80`](#insn-00ac8d80) → [`00ac8f7c`](#insn-00ac8f7c)
  - `FALL_THROUGH` [`00ac8d80`](#insn-00ac8d80) → [`00ac8d84`](#insn-00ac8d84)
- ブロック [`00ac8d84`](#insn-00ac8d84) 範囲 `[['00ac8d84', '00ac8daf']]`
  - `CONDITIONAL_JUMP` [`00ac8dac`](#insn-00ac8dac) → [`00ac8fe4`](#insn-00ac8fe4)
  - `FALL_THROUGH` [`00ac8dac`](#insn-00ac8dac) → [`00ac8db0`](#insn-00ac8db0)
- ブロック [`00ac8db0`](#insn-00ac8db0) 範囲 `[['00ac8db0', '00ac8dbf']]`
  - `UNCONDITIONAL_JUMP` [`00ac8dbc`](#insn-00ac8dbc) → [`00ac8f7c`](#insn-00ac8f7c)
- ブロック [`00ac8dc0`](#insn-00ac8dc0) 範囲 `[['00ac8dc0', '00ac8dcf']]`
  - `CONDITIONAL_JUMP` [`00ac8dcc`](#insn-00ac8dcc) → [`00ac8f7c`](#insn-00ac8f7c)
  - `FALL_THROUGH` [`00ac8dcc`](#insn-00ac8dcc) → [`00ac8dd0`](#insn-00ac8dd0)
- ブロック [`00ac8dd0`](#insn-00ac8dd0) 範囲 `[['00ac8dd0', '00ac8def']]`
  - `CONDITIONAL_JUMP` [`00ac8dec`](#insn-00ac8dec) → [`00ac8e2c`](#insn-00ac8e2c)
  - `FALL_THROUGH` [`00ac8dec`](#insn-00ac8dec) → [`00ac8df0`](#insn-00ac8df0)
- ブロック [`00ac8df0`](#insn-00ac8df0) 範囲 `[['00ac8df0', '00ac8e2b']]`
  - `FALL_THROUGH` [`00ac8e28`](#insn-00ac8e28) → [`00ac8e2c`](#insn-00ac8e2c)
- ブロック [`00ac8e2c`](#insn-00ac8e2c) 範囲 `[['00ac8e2c', '00ac8e43']]`
  - `CONDITIONAL_JUMP` [`00ac8e40`](#insn-00ac8e40) → [`00ac8e90`](#insn-00ac8e90)
  - `FALL_THROUGH` [`00ac8e40`](#insn-00ac8e40) → [`00ac8e44`](#insn-00ac8e44)
- ブロック [`00ac8e44`](#insn-00ac8e44) 範囲 `[['00ac8e44', '00ac8e8f']]`
  - `FALL_THROUGH` [`00ac8e8c`](#insn-00ac8e8c) → [`00ac8e90`](#insn-00ac8e90)
- ブロック [`00ac8e90`](#insn-00ac8e90) 範囲 `[['00ac8e90', '00ac8eb3']]`
  - `CONDITIONAL_JUMP` [`00ac8eb0`](#insn-00ac8eb0) → [`00ac8f48`](#insn-00ac8f48)
  - `FALL_THROUGH` [`00ac8eb0`](#insn-00ac8eb0) → [`00ac8eb4`](#insn-00ac8eb4)
- ブロック [`00ac8eb4`](#insn-00ac8eb4) 範囲 `[['00ac8eb4', '00ac8eeb']]`
  - `CONDITIONAL_JUMP` [`00ac8ee8`](#insn-00ac8ee8) → [`00ac8ef4`](#insn-00ac8ef4)
  - `FALL_THROUGH` [`00ac8ee8`](#insn-00ac8ee8) → [`00ac8eec`](#insn-00ac8eec)
- ブロック [`00ac8eec`](#insn-00ac8eec) 範囲 `[['00ac8eec', '00ac8ef3']]`
  - `CONDITIONAL_JUMP` [`00ac8ef0`](#insn-00ac8ef0) → [`00ac8f7c`](#insn-00ac8f7c)
  - `FALL_THROUGH` [`00ac8ef0`](#insn-00ac8ef0) → [`00ac8ef4`](#insn-00ac8ef4)
- ブロック [`00ac8ef4`](#insn-00ac8ef4) 範囲 `[['00ac8ef4', '00ac8f1f']]`
  - `CONDITIONAL_JUMP` [`00ac8f1c`](#insn-00ac8f1c) → [`00ac8fe4`](#insn-00ac8fe4)
  - `FALL_THROUGH` [`00ac8f1c`](#insn-00ac8f1c) → [`00ac8f20`](#insn-00ac8f20)
- ブロック [`00ac8f20`](#insn-00ac8f20) 範囲 `[['00ac8f20', '00ac8f33']]`
  - `UNCONDITIONAL_JUMP` [`00ac8f30`](#insn-00ac8f30) → [`00ac8fd4`](#insn-00ac8fd4)
- ブロック [`00ac8f34`](#insn-00ac8f34) 範囲 `[['00ac8f34', '00ac8f47']]`
  - `UNCONDITIONAL_JUMP` [`00ac8f44`](#insn-00ac8f44) → [`00ac8f6c`](#insn-00ac8f6c)
- ブロック [`00ac8f48`](#insn-00ac8f48) 範囲 `[['00ac8f48', '00ac8f6b']]`
  - `FALL_THROUGH` [`00ac8f68`](#insn-00ac8f68) → [`00ac8f6c`](#insn-00ac8f6c)
- ブロック [`00ac8f6c`](#insn-00ac8f6c) 範囲 `[['00ac8f6c', '00ac8f7b']]`
  - `FALL_THROUGH` [`00ac8f78`](#insn-00ac8f78) → [`00ac8f7c`](#insn-00ac8f7c)
- ブロック [`00ac8f7c`](#insn-00ac8f7c) 範囲 `[['00ac8f7c', '00ac8f87']]`
  - `CONDITIONAL_JUMP` [`00ac8f84`](#insn-00ac8f84) → [`00ac8fa8`](#insn-00ac8fa8)
  - `FALL_THROUGH` [`00ac8f84`](#insn-00ac8f84) → [`00ac8f88`](#insn-00ac8f88)
- ブロック [`00ac8f88`](#insn-00ac8f88) 範囲 `[['00ac8f88', '00ac8f8f']]`
  - `CONDITIONAL_JUMP` [`00ac8f8c`](#insn-00ac8f8c) → [`00ac8fc8`](#insn-00ac8fc8)
  - `FALL_THROUGH` [`00ac8f8c`](#insn-00ac8f8c) → [`00ac8f90`](#insn-00ac8f90)
- ブロック [`00ac8f90`](#insn-00ac8f90) 範囲 `[['00ac8f90', '00ac8f9f']]`
  - `CONDITIONAL_JUMP` [`00ac8f9c`](#insn-00ac8f9c) → [`00ac8fc8`](#insn-00ac8fc8)
  - `FALL_THROUGH` [`00ac8f9c`](#insn-00ac8f9c) → [`00ac8fa0`](#insn-00ac8fa0)
- ブロック [`00ac8fa0`](#insn-00ac8fa0) 範囲 `[['00ac8fa0', '00ac8fa7']]`
  - `UNCONDITIONAL_JUMP` [`00ac8fa4`](#insn-00ac8fa4) → [`00ac8fc4`](#insn-00ac8fc4)
- ブロック [`00ac8fa8`](#insn-00ac8fa8) 範囲 `[['00ac8fa8', '00ac8fbf']]`
  - `CONDITIONAL_JUMP` [`00ac8fbc`](#insn-00ac8fbc) → [`00ac8fc8`](#insn-00ac8fc8)
  - `FALL_THROUGH` [`00ac8fbc`](#insn-00ac8fbc) → [`00ac8fc0`](#insn-00ac8fc0)
- ブロック [`00ac8fc0`](#insn-00ac8fc0) 範囲 `[['00ac8fc0', '00ac8fc3']]`
  - `FALL_THROUGH` [`00ac8fc0`](#insn-00ac8fc0) → [`00ac8fc4`](#insn-00ac8fc4)
- ブロック [`00ac8fc4`](#insn-00ac8fc4) 範囲 `[['00ac8fc4', '00ac8fc7']]`
  - `FALL_THROUGH` [`00ac8fc4`](#insn-00ac8fc4) → [`00ac8fc8`](#insn-00ac8fc8)
- ブロック [`00ac8fc8`](#insn-00ac8fc8) 範囲 `[['00ac8fc8', '00ac8fcf']]`
  - `FALL_THROUGH` [`00ac8fcc`](#insn-00ac8fcc) → [`00ac8fd0`](#insn-00ac8fd0)
- ブロック [`00ac8fd0`](#insn-00ac8fd0) 範囲 `[['00ac8fd0', '00ac8fd3']]`
  - `FALL_THROUGH` [`00ac8fd0`](#insn-00ac8fd0) → [`00ac8fd4`](#insn-00ac8fd4)
- ブロック [`00ac8fd4`](#insn-00ac8fd4) 範囲 `[['00ac8fd4', '00ac8fe3']]`
- ブロック [`00ac8fe4`](#insn-00ac8fe4) 範囲 `[['00ac8fe4', '00ac8fe7']]`

## 命令位置別の参照

- [`00ac8bec`](#insn-00ac8bec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8bf0`](#insn-00ac8bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8bf4`](#insn-00ac8bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c0c`](#insn-00ac8c0c) → [`00ac8c18`](#insn-00ac8c18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c1c`](#insn-00ac8c1c) → [`00ac8c54`](#insn-00ac8c54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c30`](#insn-00ac8c30) → [`00ac8fd0`](#insn-00ac8fd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c38`](#insn-00ac8c38) → [`00ac8fe4`](#insn-00ac8fe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c50`](#insn-00ac8c50) → [`00ac8fd4`](#insn-00ac8fd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c54`](#insn-00ac8c54) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c60`](#insn-00ac8c60) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8c64`](#insn-00ac8c64) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c68`](#insn-00ac8c68) → [`00ac8dc0`](#insn-00ac8dc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c78`](#insn-00ac8c78) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8c80`](#insn-00ac8c80) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8c84`](#insn-00ac8c84) → [`00ac8ca8`](#insn-00ac8ca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c88`](#insn-00ac8c88) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8c98`](#insn-00ac8c98) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8ca0`](#insn-00ac8ca0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ca4`](#insn-00ac8ca4) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8ca8`](#insn-00ac8ca8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8cb4`](#insn-00ac8cb4) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8cbc`](#insn-00ac8cbc) → [`00ac8d1c`](#insn-00ac8d1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8cc0`](#insn-00ac8cc0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8cd0`](#insn-00ac8cd0) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8cd4`](#insn-00ac8cd4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ce0`](#insn-00ac8ce0) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8cf0`](#insn-00ac8cf0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8cf4`](#insn-00ac8cf4) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8cf8`](#insn-00ac8cf8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d04`](#insn-00ac8d04) → `00333fa0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d14`](#insn-00ac8d14) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d18`](#insn-00ac8d18) → `00333fa0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d1c`](#insn-00ac8d1c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d28`](#insn-00ac8d28) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d2c`](#insn-00ac8d2c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d30`](#insn-00ac8d30) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d34`](#insn-00ac8d34) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d3c`](#insn-00ac8d3c) → [`00ac8f34`](#insn-00ac8f34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d44`](#insn-00ac8d44) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d48`](#insn-00ac8d48) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d4c`](#insn-00ac8d4c) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d54`](#insn-00ac8d54) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d60`](#insn-00ac8d60) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d64`](#insn-00ac8d64) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d70`](#insn-00ac8d70) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d78`](#insn-00ac8d78) → [`00ac8d84`](#insn-00ac8d84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d80`](#insn-00ac8d80) → [`00ac8f7c`](#insn-00ac8f7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d84`](#insn-00ac8d84) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8d90`](#insn-00ac8d90) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8d94`](#insn-00ac8d94) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8da8`](#insn-00ac8da8) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8dac`](#insn-00ac8dac) → [`00ac8fe4`](#insn-00ac8fe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8dbc`](#insn-00ac8dbc) → [`00ac8f7c`](#insn-00ac8f7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8dc8`](#insn-00ac8dc8) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8dcc`](#insn-00ac8dcc) → [`00ac8f7c`](#insn-00ac8f7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8dd0`](#insn-00ac8dd0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8de0`](#insn-00ac8de0) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8de8`](#insn-00ac8de8) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8dec`](#insn-00ac8dec) → [`00ac8e2c`](#insn-00ac8e2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8df0`](#insn-00ac8df0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e00`](#insn-00ac8e00) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e08`](#insn-00ac8e08) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e0c`](#insn-00ac8e0c) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e10`](#insn-00ac8e10) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e1c`](#insn-00ac8e1c) → `00333fa0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e24`](#insn-00ac8e24) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e28`](#insn-00ac8e28) → `00333fa0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e2c`](#insn-00ac8e2c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e38`](#insn-00ac8e38) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e40`](#insn-00ac8e40) → [`00ac8e90`](#insn-00ac8e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e44`](#insn-00ac8e44) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e54`](#insn-00ac8e54) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e58`](#insn-00ac8e58) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e68`](#insn-00ac8e68) → `00333fa0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e6c`](#insn-00ac8e6c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e78`](#insn-00ac8e78) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e88`](#insn-00ac8e88) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e8c`](#insn-00ac8e8c) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8e90`](#insn-00ac8e90) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8e9c`](#insn-00ac8e9c) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8ea0`](#insn-00ac8ea0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ea4`](#insn-00ac8ea4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ea8`](#insn-00ac8ea8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8eb0`](#insn-00ac8eb0) → [`00ac8f48`](#insn-00ac8f48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ec0`](#insn-00ac8ec0) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8ec4`](#insn-00ac8ec4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ed0`](#insn-00ac8ed0) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8ed4`](#insn-00ac8ed4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ee0`](#insn-00ac8ee0) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8ee8`](#insn-00ac8ee8) → [`00ac8ef4`](#insn-00ac8ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ef0`](#insn-00ac8ef0) → [`00ac8f7c`](#insn-00ac8f7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ef4`](#insn-00ac8ef4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f00`](#insn-00ac8f00) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8f04`](#insn-00ac8f04) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f18`](#insn-00ac8f18) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8f1c`](#insn-00ac8f1c) → [`00ac8fe4`](#insn-00ac8fe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f30`](#insn-00ac8f30) → [`00ac8fd4`](#insn-00ac8fd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f38`](#insn-00ac8f38) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8f3c`](#insn-00ac8f3c) → `00c9c5d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac8f40`](#insn-00ac8f40) → `00ca51fc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f44`](#insn-00ac8f44) → [`00ac8f6c`](#insn-00ac8f6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f48`](#insn-00ac8f48) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f58`](#insn-00ac8f58) → `00333f90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8f5c`](#insn-00ac8f5c) → `00c9c5d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac8f68`](#insn-00ac8f68) → `00ca522c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ac8f6c`](#insn-00ac8f6c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f78`](#insn-00ac8f78) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ac8f84`](#insn-00ac8f84) → [`00ac8fa8`](#insn-00ac8fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f8c`](#insn-00ac8f8c) → [`00ac8fc8`](#insn-00ac8fc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f9c`](#insn-00ac8f9c) → [`00ac8fc8`](#insn-00ac8fc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fa4`](#insn-00ac8fa4) → [`00ac8fc4`](#insn-00ac8fc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fb4`](#insn-00ac8fb4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fbc`](#insn-00ac8fbc) → [`00ac8fc8`](#insn-00ac8fc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fcc`](#insn-00ac8fcc) → [`00ac9044`](../00ac9/00ac9044.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9044` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fd4`](#insn-00ac8fd4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fd8`](#insn-00ac8fd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fdc`](#insn-00ac8fdc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fe4`](#insn-00ac8fe4) → [`0045a0d4`](../0045a/0045a0d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045a0d4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac8bec`](#insn-00ac8bec)

~~~json
{
  "source": "00ac8bec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8bf0`](#insn-00ac8bf0)

~~~json
{
  "source": "00ac8bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8bf4`](#insn-00ac8bf4)

~~~json
{
  "source": "00ac8bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c0c`](#insn-00ac8c0c)

~~~json
{
  "source": "00ac8c0c",
  "target": "00ac8c18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c1c`](#insn-00ac8c1c)

~~~json
{
  "source": "00ac8c1c",
  "target": "00ac8c54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c30`](#insn-00ac8c30)

~~~json
{
  "source": "00ac8c30",
  "target": "00ac8fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c38`](#insn-00ac8c38)

~~~json
{
  "source": "00ac8c38",
  "target": "00ac8fe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c50`](#insn-00ac8c50)

~~~json
{
  "source": "00ac8c50",
  "target": "00ac8fd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c54`](#insn-00ac8c54)

~~~json
{
  "source": "00ac8c54",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8c60`](#insn-00ac8c60)

~~~json
{
  "source": "00ac8c60",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8c64`](#insn-00ac8c64)

~~~json
{
  "source": "00ac8c64",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8c68`](#insn-00ac8c68)

~~~json
{
  "source": "00ac8c68",
  "target": "00ac8dc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c78`](#insn-00ac8c78)

~~~json
{
  "source": "00ac8c78",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8c80`](#insn-00ac8c80)

~~~json
{
  "source": "00ac8c80",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8c84`](#insn-00ac8c84)

~~~json
{
  "source": "00ac8c84",
  "target": "00ac8ca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8c88`](#insn-00ac8c88)

~~~json
{
  "source": "00ac8c88",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8c98`](#insn-00ac8c98)

~~~json
{
  "source": "00ac8c98",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8ca0`](#insn-00ac8ca0)

~~~json
{
  "source": "00ac8ca0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ca4`](#insn-00ac8ca4)

~~~json
{
  "source": "00ac8ca4",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8ca8`](#insn-00ac8ca8)

~~~json
{
  "source": "00ac8ca8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8cb4`](#insn-00ac8cb4)

~~~json
{
  "source": "00ac8cb4",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8cbc`](#insn-00ac8cbc)

~~~json
{
  "source": "00ac8cbc",
  "target": "00ac8d1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8cc0`](#insn-00ac8cc0)

~~~json
{
  "source": "00ac8cc0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8cd0`](#insn-00ac8cd0)

~~~json
{
  "source": "00ac8cd0",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8cd4`](#insn-00ac8cd4)

~~~json
{
  "source": "00ac8cd4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ce0`](#insn-00ac8ce0)

~~~json
{
  "source": "00ac8ce0",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8cf0`](#insn-00ac8cf0)

~~~json
{
  "source": "00ac8cf0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8cf4`](#insn-00ac8cf4)

~~~json
{
  "source": "00ac8cf4",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8cf8`](#insn-00ac8cf8)

~~~json
{
  "source": "00ac8cf8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d04`](#insn-00ac8d04)

~~~json
{
  "source": "00ac8d04",
  "target": "00333fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fa0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "249e6c00388d0900",
  "capture_start": "00333fa0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d14`](#insn-00ac8d14)

~~~json
{
  "source": "00ac8d14",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d18`](#insn-00ac8d18)

~~~json
{
  "source": "00ac8d18",
  "target": "00333fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fa0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "249e6c00388d0900",
  "capture_start": "00333fa0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d1c`](#insn-00ac8d1c)

~~~json
{
  "source": "00ac8d1c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d28`](#insn-00ac8d28)

~~~json
{
  "source": "00ac8d28",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d2c`](#insn-00ac8d2c)

~~~json
{
  "source": "00ac8d2c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d30`](#insn-00ac8d30)

~~~json
{
  "source": "00ac8d30",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d34`](#insn-00ac8d34)

~~~json
{
  "source": "00ac8d34",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d3c`](#insn-00ac8d3c)

~~~json
{
  "source": "00ac8d3c",
  "target": "00ac8f34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8d44`](#insn-00ac8d44)

~~~json
{
  "source": "00ac8d44",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d48`](#insn-00ac8d48)

~~~json
{
  "source": "00ac8d48",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d4c`](#insn-00ac8d4c)

~~~json
{
  "source": "00ac8d4c",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d54`](#insn-00ac8d54)

~~~json
{
  "source": "00ac8d54",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d60`](#insn-00ac8d60)

~~~json
{
  "source": "00ac8d60",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "a49c6c008c8c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d64`](#insn-00ac8d64)

~~~json
{
  "source": "00ac8d64",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d70`](#insn-00ac8d70)

~~~json
{
  "source": "00ac8d70",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d78`](#insn-00ac8d78)

~~~json
{
  "source": "00ac8d78",
  "target": "00ac8d84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8d80`](#insn-00ac8d80)

~~~json
{
  "source": "00ac8d80",
  "target": "00ac8f7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8d84`](#insn-00ac8d84)

~~~json
{
  "source": "00ac8d84",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8d90`](#insn-00ac8d90)

~~~json
{
  "source": "00ac8d90",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8d94`](#insn-00ac8d94)

~~~json
{
  "source": "00ac8d94",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8da8`](#insn-00ac8da8)

~~~json
{
  "source": "00ac8da8",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8dac`](#insn-00ac8dac)

~~~json
{
  "source": "00ac8dac",
  "target": "00ac8fe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8dbc`](#insn-00ac8dbc)

~~~json
{
  "source": "00ac8dbc",
  "target": "00ac8f7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8dc8`](#insn-00ac8dc8)

~~~json
{
  "source": "00ac8dc8",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8dcc`](#insn-00ac8dcc)

~~~json
{
  "source": "00ac8dcc",
  "target": "00ac8f7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8dd0`](#insn-00ac8dd0)

~~~json
{
  "source": "00ac8dd0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8de0`](#insn-00ac8de0)

~~~json
{
  "source": "00ac8de0",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8de8`](#insn-00ac8de8)

~~~json
{
  "source": "00ac8de8",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8dec`](#insn-00ac8dec)

~~~json
{
  "source": "00ac8dec",
  "target": "00ac8e2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8df0`](#insn-00ac8df0)

~~~json
{
  "source": "00ac8df0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e00`](#insn-00ac8e00)

~~~json
{
  "source": "00ac8e00",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e08`](#insn-00ac8e08)

~~~json
{
  "source": "00ac8e08",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e0c`](#insn-00ac8e0c)

~~~json
{
  "source": "00ac8e0c",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e10`](#insn-00ac8e10)

~~~json
{
  "source": "00ac8e10",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e1c`](#insn-00ac8e1c)

~~~json
{
  "source": "00ac8e1c",
  "target": "00333fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fa0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "249e6c00388d0900",
  "capture_start": "00333fa0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e24`](#insn-00ac8e24)

~~~json
{
  "source": "00ac8e24",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e28`](#insn-00ac8e28)

~~~json
{
  "source": "00ac8e28",
  "target": "00333fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fa0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "249e6c00388d0900",
  "capture_start": "00333fa0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e2c`](#insn-00ac8e2c)

~~~json
{
  "source": "00ac8e2c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e38`](#insn-00ac8e38)

~~~json
{
  "source": "00ac8e38",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e40`](#insn-00ac8e40)

~~~json
{
  "source": "00ac8e40",
  "target": "00ac8e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8e44`](#insn-00ac8e44)

~~~json
{
  "source": "00ac8e44",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e54`](#insn-00ac8e54)

~~~json
{
  "source": "00ac8e54",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e58`](#insn-00ac8e58)

~~~json
{
  "source": "00ac8e58",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e68`](#insn-00ac8e68)

~~~json
{
  "source": "00ac8e68",
  "target": "00333fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fa0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "249e6c00388d0900",
  "capture_start": "00333fa0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e6c`](#insn-00ac8e6c)

~~~json
{
  "source": "00ac8e6c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e78`](#insn-00ac8e78)

~~~json
{
  "source": "00ac8e78",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e88`](#insn-00ac8e88)

~~~json
{
  "source": "00ac8e88",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e8c`](#insn-00ac8e8c)

~~~json
{
  "source": "00ac8e8c",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8e90`](#insn-00ac8e90)

~~~json
{
  "source": "00ac8e90",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8e9c`](#insn-00ac8e9c)

~~~json
{
  "source": "00ac8e9c",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8ea0`](#insn-00ac8ea0)

~~~json
{
  "source": "00ac8ea0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ea4`](#insn-00ac8ea4)

~~~json
{
  "source": "00ac8ea4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ea8`](#insn-00ac8ea8)

~~~json
{
  "source": "00ac8ea8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8eb0`](#insn-00ac8eb0)

~~~json
{
  "source": "00ac8eb0",
  "target": "00ac8f48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ec0`](#insn-00ac8ec0)

~~~json
{
  "source": "00ac8ec0",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8ec4`](#insn-00ac8ec4)

~~~json
{
  "source": "00ac8ec4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ed0`](#insn-00ac8ed0)

~~~json
{
  "source": "00ac8ed0",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "a49c6c008c8c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8ed4`](#insn-00ac8ed4)

~~~json
{
  "source": "00ac8ed4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ee0`](#insn-00ac8ee0)

~~~json
{
  "source": "00ac8ee0",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8ee8`](#insn-00ac8ee8)

~~~json
{
  "source": "00ac8ee8",
  "target": "00ac8ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ef0`](#insn-00ac8ef0)

~~~json
{
  "source": "00ac8ef0",
  "target": "00ac8f7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ef4`](#insn-00ac8ef4)

~~~json
{
  "source": "00ac8ef4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f00`](#insn-00ac8f00)

~~~json
{
  "source": "00ac8f00",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8f04`](#insn-00ac8f04)

~~~json
{
  "source": "00ac8f04",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f18`](#insn-00ac8f18)

~~~json
{
  "source": "00ac8f18",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8f1c`](#insn-00ac8f1c)

~~~json
{
  "source": "00ac8f1c",
  "target": "00ac8fe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f30`](#insn-00ac8f30)

~~~json
{
  "source": "00ac8f30",
  "target": "00ac8fd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f38`](#insn-00ac8f38)

~~~json
{
  "source": "00ac8f38",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8f3c`](#insn-00ac8f3c)

~~~json
{
  "source": "00ac8f3c",
  "target": "00c9c5d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c5d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac8f40`](#insn-00ac8f40)

~~~json
{
  "source": "00ac8f40",
  "target": "00ca51fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f44`](#insn-00ac8f44)

~~~json
{
  "source": "00ac8f44",
  "target": "00ac8f6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f48`](#insn-00ac8f48)

~~~json
{
  "source": "00ac8f48",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f58`](#insn-00ac8f58)

~~~json
{
  "source": "00ac8f58",
  "target": "00333f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "fc9d6c00fc8c0900",
  "capture_start": "00333f90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8f5c`](#insn-00ac8f5c)

~~~json
{
  "source": "00ac8f5c",
  "target": "00c9c5d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c5d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac8f68`](#insn-00ac8f68)

~~~json
{
  "source": "00ac8f68",
  "target": "00ca522c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca522c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac8f6c`](#insn-00ac8f6c)

~~~json
{
  "source": "00ac8f6c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f78`](#insn-00ac8f78)

~~~json
{
  "source": "00ac8f78",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "a49c6c008c8c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac8f84`](#insn-00ac8f84)

~~~json
{
  "source": "00ac8f84",
  "target": "00ac8fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f8c`](#insn-00ac8f8c)

~~~json
{
  "source": "00ac8f8c",
  "target": "00ac8fc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f9c`](#insn-00ac8f9c)

~~~json
{
  "source": "00ac8f9c",
  "target": "00ac8fc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fa4`](#insn-00ac8fa4)

~~~json
{
  "source": "00ac8fa4",
  "target": "00ac8fc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fb4`](#insn-00ac8fb4)

~~~json
{
  "source": "00ac8fb4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8fbc`](#insn-00ac8fbc)

~~~json
{
  "source": "00ac8fbc",
  "target": "00ac8fc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fcc`](#insn-00ac8fcc)

~~~json
{
  "source": "00ac8fcc",
  "target": "00ac9044",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8fd4`](#insn-00ac8fd4)

~~~json
{
  "source": "00ac8fd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fd8`](#insn-00ac8fd8)

~~~json
{
  "source": "00ac8fd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fdc`](#insn-00ac8fdc)

~~~json
{
  "source": "00ac8fdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fe4`](#insn-00ac8fe4)

~~~json
{
  "source": "00ac8fe4",
  "target": "0045a0d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
