# 00aa2afc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aa2900`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2900.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-f6be05fbee8bf99b07588a48e2e293ef)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aa2b6c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa2/00aa2b6c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-edbfe84451034b7a1031c3177317769a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2afc",
  "name": "FUN_00aa2afc",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ca950bf56df8f3f30f01aa64a817e2c7634f94799edb6fc9b3693cf81ea171ee",
  "source_text_sha256": "ca950bf56df8f3f30f01aa64a817e2c7634f94799edb6fc9b3693cf81ea171ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa2afc",
        "00aa2cef"
      ]
    ],
    "bytes_sha256": "d3f0909cb68e2f3ee2af50f9048ad3b49f1d82d83a8f44b2497d43419d744c41",
    "instruction_count": 125,
    "instruction_bytes": 500,
    "body_bytes": 500,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a261bc](../00a26/00a261bc.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [00480118](../00480/00480118.md)
- [00480178](../00480/00480178.md)
- [004801d8](../00480/004801d8.md)
- [0086be6c](../0086b/0086be6c.md)
- [00c57e90](../00c57/00c57e90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3100 bytes

~~~c

void FUN_00aa2afc(long param_1,undefined8 param_2)

{
  char cVar1;
  short sVar2;
  int iVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long *plVar6;
  long *plVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  int iVar10;
  undefined8 *puVar11;
  
  puVar9 = (undefined8 *)(param_1 + 0x20);
  plVar7 = (long *)(param_1 + 0x18);
  FUN_0086be6c(plVar7,*puVar9);
  *puVar9 = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  *(undefined8 **)(param_1 + 0x18) = puVar9;
  sVar2 = FUN_00480178(param_2);
  if (0 < sVar2) {
    iVar10 = 0;
    do {
      iVar3 = FUN_004801d8(param_2);
      cVar1 = FUN_00480118(param_2);
      puVar5 = (undefined8 *)*puVar9;
      puVar8 = puVar9;
      puVar11 = puVar9;
      if ((undefined8 *)*puVar9 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar8 = puVar4, iVar3 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar11 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00aa2be8;
          }
          if (iVar3 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00aa2c38;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar11 = puVar4 + 1;
      }
LAB_00aa2be8:
      puVar4 = (undefined8 *)_Znwm(0x28);
      puVar4[4] = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar8;
      *puVar11 = puVar4;
      plVar6 = (long *)*plVar7;
      *(int *)((long)puVar4 + 0x1c) = iVar3;
      puVar5 = puVar4;
      if (*plVar6 != 0) {
        *plVar7 = *plVar6;
        puVar5 = (undefined8 *)*puVar11;
      }
      FUN_0043bba4(*(undefined8 *)(param_1 + 0x20),puVar5);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aa2c38:
      *(int *)(puVar4 + 4) = (int)cVar1;
      cVar1 = FUN_00480118(param_2);
      puVar5 = (undefined8 *)*puVar9;
      puVar8 = puVar9;
      puVar11 = puVar9;
      if ((undefined8 *)*puVar9 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar8 = puVar4, iVar3 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar11 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00aa2c90;
          }
          if (iVar3 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00aa2b74;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar11 = puVar4 + 1;
      }
LAB_00aa2c90:
      puVar4 = (undefined8 *)_Znwm(0x28);
      puVar4[4] = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar8;
      *puVar11 = puVar4;
      plVar6 = (long *)*plVar7;
      *(int *)((long)puVar4 + 0x1c) = iVar3;
      puVar5 = puVar4;
      if (*plVar6 != 0) {
        *plVar7 = *plVar6;
        puVar5 = (undefined8 *)*puVar11;
      }
      FUN_0043bba4(*(undefined8 *)(param_1 + 0x20),puVar5);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aa2b74:
      iVar10 = iVar10 + 1;
      *(int *)((long)puVar4 + 0x24) = (int)cVar1;
    } while (iVar10 != sVar2);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa2afc"></a> `00aa2afc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aa2b00"></a> `00aa2b00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2b04"></a> `00aa2b04` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2b08"></a> `00aa2b08` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa2b0c"></a> `00aa2b0c` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa2b10"></a> `00aa2b10` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa2b14"></a> `00aa2b14` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa2b18"></a> `00aa2b18` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aa2b1c"></a> `00aa2b1c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00aa2b20"></a> `00aa2b20` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aa2b24"></a> `00aa2b24` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aa2b28"></a> `00aa2b28` | `21 0f 42 f8` | ldr x1,[x25, #0x20]! | `FALL_THROUGH`
<a id="insn-00aa2b2c"></a> `00aa2b2c` | `35 23 00 d1` | sub x21,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00aa2b30"></a> `00aa2b30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aa2b34"></a> `00aa2b34` | `ce 24 f7 97` | bl 0x0086be6c | `UNCONDITIONAL_CALL`
<a id="insn-00aa2b38"></a> `00aa2b38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa2b3c"></a> `00aa2b3c` | `3f 7f 00 a9` | stp xzr,xzr,[x25] | `FALL_THROUGH`
<a id="insn-00aa2b40"></a> `00aa2b40` | `39 83 1f f8` | stur x25,[x25, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa2b44"></a> `00aa2b44` | `8d 75 e7 97` | bl 0x00480178 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2b48"></a> `00aa2b48` | `08 3c 00 13` | sxth w8,w0 | `FALL_THROUGH`
<a id="insn-00aa2b4c"></a> `00aa2b4c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aa2b50"></a> `00aa2b50` | `a8 c3 1f b8` | stur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00aa2b54"></a> `00aa2b54` | `eb 0b 00 54` | b.lt 0x00aa2cd0 | `CONDITIONAL_JUMP`
<a id="insn-00aa2b58"></a> `00aa2b58` | `fb 03 1f 2a` | mov w27,wzr | `FALL_THROUGH`
<a id="insn-00aa2b5c"></a> `00aa2b5c` | `0c 00 00 14` | b 0x00aa2b8c | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2b60"></a> `00aa2b60` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2b64"></a> `00aa2b64` | `10 64 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2b68"></a> `00aa2b68` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aa2b6c"></a> `00aa2b6c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aa2b70"></a> `00aa2b70` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aa2b74"></a> `00aa2b74` | `a9 c3 5f b8` | ldur w9,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00aa2b78"></a> `00aa2b78` | `e8 1e 00 13` | sxtb w8,w23 | `FALL_THROUGH`
<a id="insn-00aa2b7c"></a> `00aa2b7c` | `7b 07 00 11` | add w27,w27,#0x1 | `FALL_THROUGH`
<a id="insn-00aa2b80"></a> `00aa2b80` | `7f 03 09 6b` | cmp w27,w9 | `FALL_THROUGH`
<a id="insn-00aa2b84"></a> `00aa2b84` | `08 27 00 b9` | str w8,[x24, #0x24] | `FALL_THROUGH`
<a id="insn-00aa2b88"></a> `00aa2b88` | `40 0a 00 54` | b.eq 0x00aa2cd0 | `CONDITIONAL_JUMP`
<a id="insn-00aa2b8c"></a> `00aa2b8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa2b90"></a> `00aa2b90` | `92 75 e7 97` | bl 0x004801d8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2b94"></a> `00aa2b94` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa2b98"></a> `00aa2b98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa2b9c"></a> `00aa2b9c` | `5f 75 e7 97` | bl 0x00480118 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2ba0"></a> `00aa2ba0` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00aa2ba4"></a> `00aa2ba4` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aa2ba8"></a> `00aa2ba8` | `fc 03 19 aa` | mov x28,x25 | `FALL_THROUGH`
<a id="insn-00aa2bac"></a> `00aa2bac` | `f8 03 19 aa` | mov x24,x25 | `FALL_THROUGH`
<a id="insn-00aa2bb0"></a> `00aa2bb0` | `a8 00 00 b5` | cbnz x8,0x00aa2bc4 | `CONDITIONAL_JUMP`
<a id="insn-00aa2bb4"></a> `00aa2bb4` | `0d 00 00 14` | b 0x00aa2be8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2bb8"></a> `00aa2bb8` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00aa2bbc"></a> `00aa2bbc` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00aa2bc0"></a> `00aa2bc0` | `48 01 00 b4` | cbz x8,0x00aa2be8 | `CONDITIONAL_JUMP`
<a id="insn-00aa2bc4"></a> `00aa2bc4` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00aa2bc8"></a> `00aa2bc8` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2bcc"></a> `00aa2bcc` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00aa2bd0"></a> `00aa2bd0` | `4b ff ff 54` | b.lt 0x00aa2bb8 | `CONDITIONAL_JUMP`
<a id="insn-00aa2bd4"></a> `00aa2bd4` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00aa2bd8"></a> `00aa2bd8` | `0a 03 00 54` | b.ge 0x00aa2c38 | `CONDITIONAL_JUMP`
<a id="insn-00aa2bdc"></a> `00aa2bdc` | `08 07 40 f9` | ldr x8,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00aa2be0"></a> `00aa2be0` | `28 ff ff b5` | cbnz x8,0x00aa2bc4 | `CONDITIONAL_JUMP`
<a id="insn-00aa2be4"></a> `00aa2be4` | `1c 23 00 91` | add x28,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00aa2be8"></a> `00aa2be8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aa2bec"></a> `00aa2bec` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-00aa2bf0"></a> `00aa2bf0` | `a8 d4 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2bf4"></a> `00aa2bf4` | `1f 10 00 f9` | str xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2bf8"></a> `00aa2bf8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00aa2bfc"></a> `00aa2bfc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aa2c00"></a> `00aa2c00` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aa2c04"></a> `00aa2c04` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2c08"></a> `00aa2c08` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00aa2c0c"></a> `00aa2c0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00aa2c10"></a> `00aa2c10` | `16 1c 00 b9` | str w22,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2c14"></a> `00aa2c14` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aa2c18"></a> `00aa2c18` | `68 00 00 b4` | cbz x8,0x00aa2c24 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c1c"></a> `00aa2c1c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00aa2c20"></a> `00aa2c20` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00aa2c24"></a> `00aa2c24` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2c28"></a> `00aa2c28` | `df 63 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2c2c"></a> `00aa2c2c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aa2c30"></a> `00aa2c30` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aa2c34"></a> `00aa2c34` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aa2c38"></a> `00aa2c38` | `e8 1e 00 13` | sxtb w8,w23 | `FALL_THROUGH`
<a id="insn-00aa2c3c"></a> `00aa2c3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa2c40"></a> `00aa2c40` | `08 23 00 b9` | str w8,[x24, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2c44"></a> `00aa2c44` | `35 75 e7 97` | bl 0x00480118 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2c48"></a> `00aa2c48` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00aa2c4c"></a> `00aa2c4c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aa2c50"></a> `00aa2c50` | `fc 03 19 aa` | mov x28,x25 | `FALL_THROUGH`
<a id="insn-00aa2c54"></a> `00aa2c54` | `f8 03 19 aa` | mov x24,x25 | `FALL_THROUGH`
<a id="insn-00aa2c58"></a> `00aa2c58` | `a8 00 00 b5` | cbnz x8,0x00aa2c6c | `CONDITIONAL_JUMP`
<a id="insn-00aa2c5c"></a> `00aa2c5c` | `0d 00 00 14` | b 0x00aa2c90 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2c60"></a> `00aa2c60` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00aa2c64"></a> `00aa2c64` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00aa2c68"></a> `00aa2c68` | `48 01 00 b4` | cbz x8,0x00aa2c90 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c6c"></a> `00aa2c6c` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00aa2c70"></a> `00aa2c70` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2c74"></a> `00aa2c74` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00aa2c78"></a> `00aa2c78` | `4b ff ff 54` | b.lt 0x00aa2c60 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c7c"></a> `00aa2c7c` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00aa2c80"></a> `00aa2c80` | `aa f7 ff 54` | b.ge 0x00aa2b74 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c84"></a> `00aa2c84` | `08 07 40 f9` | ldr x8,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00aa2c88"></a> `00aa2c88` | `28 ff ff b5` | cbnz x8,0x00aa2c6c | `CONDITIONAL_JUMP`
<a id="insn-00aa2c8c"></a> `00aa2c8c` | `1c 23 00 91` | add x28,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00aa2c90"></a> `00aa2c90` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aa2c94"></a> `00aa2c94` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-00aa2c98"></a> `00aa2c98` | `7e d4 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2c9c"></a> `00aa2c9c` | `1f 10 00 f9` | str xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2ca0"></a> `00aa2ca0` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00aa2ca4"></a> `00aa2ca4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aa2ca8"></a> `00aa2ca8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aa2cac"></a> `00aa2cac` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2cb0"></a> `00aa2cb0` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00aa2cb4"></a> `00aa2cb4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00aa2cb8"></a> `00aa2cb8` | `16 1c 00 b9` | str w22,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2cbc"></a> `00aa2cbc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aa2cc0"></a> `00aa2cc0` | `08 f5 ff b4` | cbz x8,0x00aa2b60 | `CONDITIONAL_JUMP`
<a id="insn-00aa2cc4"></a> `00aa2cc4` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00aa2cc8"></a> `00aa2cc8` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00aa2ccc"></a> `00aa2ccc` | `a5 ff ff 17` | b 0x00aa2b60 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2cd0"></a> `00aa2cd0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa2cd4"></a> `00aa2cd4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa2cd8"></a> `00aa2cd8` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa2cdc"></a> `00aa2cdc` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa2ce0"></a> `00aa2ce0` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2ce4"></a> `00aa2ce4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2ce8"></a> `00aa2ce8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aa2cec"></a> `00aa2cec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa2afc`](#insn-00aa2afc) 範囲 `[['00aa2afc', '00aa2b57']]`
  - `CONDITIONAL_JUMP` [`00aa2b54`](#insn-00aa2b54) → [`00aa2cd0`](#insn-00aa2cd0)
  - `FALL_THROUGH` [`00aa2b54`](#insn-00aa2b54) → [`00aa2b58`](#insn-00aa2b58)
- ブロック [`00aa2b58`](#insn-00aa2b58) 範囲 `[['00aa2b58', '00aa2b5f']]`
  - `UNCONDITIONAL_JUMP` [`00aa2b5c`](#insn-00aa2b5c) → [`00aa2b8c`](#insn-00aa2b8c)
- ブロック [`00aa2b60`](#insn-00aa2b60) 範囲 `[['00aa2b60', '00aa2b73']]`
  - `FALL_THROUGH` [`00aa2b70`](#insn-00aa2b70) → [`00aa2b74`](#insn-00aa2b74)
- ブロック [`00aa2b74`](#insn-00aa2b74) 範囲 `[['00aa2b74', '00aa2b8b']]`
  - `CONDITIONAL_JUMP` [`00aa2b88`](#insn-00aa2b88) → [`00aa2cd0`](#insn-00aa2cd0)
  - `FALL_THROUGH` [`00aa2b88`](#insn-00aa2b88) → [`00aa2b8c`](#insn-00aa2b8c)
- ブロック [`00aa2b8c`](#insn-00aa2b8c) 範囲 `[['00aa2b8c', '00aa2bb3']]`
  - `CONDITIONAL_JUMP` [`00aa2bb0`](#insn-00aa2bb0) → [`00aa2bc4`](#insn-00aa2bc4)
  - `FALL_THROUGH` [`00aa2bb0`](#insn-00aa2bb0) → [`00aa2bb4`](#insn-00aa2bb4)
- ブロック [`00aa2bb4`](#insn-00aa2bb4) 範囲 `[['00aa2bb4', '00aa2bb7']]`
  - `UNCONDITIONAL_JUMP` [`00aa2bb4`](#insn-00aa2bb4) → [`00aa2be8`](#insn-00aa2be8)
- ブロック [`00aa2bb8`](#insn-00aa2bb8) 範囲 `[['00aa2bb8', '00aa2bc3']]`
  - `CONDITIONAL_JUMP` [`00aa2bc0`](#insn-00aa2bc0) → [`00aa2be8`](#insn-00aa2be8)
  - `FALL_THROUGH` [`00aa2bc0`](#insn-00aa2bc0) → [`00aa2bc4`](#insn-00aa2bc4)
- ブロック [`00aa2bc4`](#insn-00aa2bc4) 範囲 `[['00aa2bc4', '00aa2bd3']]`
  - `CONDITIONAL_JUMP` [`00aa2bd0`](#insn-00aa2bd0) → [`00aa2bb8`](#insn-00aa2bb8)
  - `FALL_THROUGH` [`00aa2bd0`](#insn-00aa2bd0) → [`00aa2bd4`](#insn-00aa2bd4)
- ブロック [`00aa2bd4`](#insn-00aa2bd4) 範囲 `[['00aa2bd4', '00aa2bdb']]`
  - `CONDITIONAL_JUMP` [`00aa2bd8`](#insn-00aa2bd8) → [`00aa2c38`](#insn-00aa2c38)
  - `FALL_THROUGH` [`00aa2bd8`](#insn-00aa2bd8) → [`00aa2bdc`](#insn-00aa2bdc)
- ブロック [`00aa2bdc`](#insn-00aa2bdc) 範囲 `[['00aa2bdc', '00aa2be3']]`
  - `CONDITIONAL_JUMP` [`00aa2be0`](#insn-00aa2be0) → [`00aa2bc4`](#insn-00aa2bc4)
  - `FALL_THROUGH` [`00aa2be0`](#insn-00aa2be0) → [`00aa2be4`](#insn-00aa2be4)
- ブロック [`00aa2be4`](#insn-00aa2be4) 範囲 `[['00aa2be4', '00aa2be7']]`
  - `FALL_THROUGH` [`00aa2be4`](#insn-00aa2be4) → [`00aa2be8`](#insn-00aa2be8)
- ブロック [`00aa2be8`](#insn-00aa2be8) 範囲 `[['00aa2be8', '00aa2c1b']]`
  - `CONDITIONAL_JUMP` [`00aa2c18`](#insn-00aa2c18) → [`00aa2c24`](#insn-00aa2c24)
  - `FALL_THROUGH` [`00aa2c18`](#insn-00aa2c18) → [`00aa2c1c`](#insn-00aa2c1c)
- ブロック [`00aa2c1c`](#insn-00aa2c1c) 範囲 `[['00aa2c1c', '00aa2c23']]`
  - `FALL_THROUGH` [`00aa2c20`](#insn-00aa2c20) → [`00aa2c24`](#insn-00aa2c24)
- ブロック [`00aa2c24`](#insn-00aa2c24) 範囲 `[['00aa2c24', '00aa2c37']]`
  - `FALL_THROUGH` [`00aa2c34`](#insn-00aa2c34) → [`00aa2c38`](#insn-00aa2c38)
- ブロック [`00aa2c38`](#insn-00aa2c38) 範囲 `[['00aa2c38', '00aa2c5b']]`
  - `CONDITIONAL_JUMP` [`00aa2c58`](#insn-00aa2c58) → [`00aa2c6c`](#insn-00aa2c6c)
  - `FALL_THROUGH` [`00aa2c58`](#insn-00aa2c58) → [`00aa2c5c`](#insn-00aa2c5c)
- ブロック [`00aa2c5c`](#insn-00aa2c5c) 範囲 `[['00aa2c5c', '00aa2c5f']]`
  - `UNCONDITIONAL_JUMP` [`00aa2c5c`](#insn-00aa2c5c) → [`00aa2c90`](#insn-00aa2c90)
- ブロック [`00aa2c60`](#insn-00aa2c60) 範囲 `[['00aa2c60', '00aa2c6b']]`
  - `CONDITIONAL_JUMP` [`00aa2c68`](#insn-00aa2c68) → [`00aa2c90`](#insn-00aa2c90)
  - `FALL_THROUGH` [`00aa2c68`](#insn-00aa2c68) → [`00aa2c6c`](#insn-00aa2c6c)
- ブロック [`00aa2c6c`](#insn-00aa2c6c) 範囲 `[['00aa2c6c', '00aa2c7b']]`
  - `CONDITIONAL_JUMP` [`00aa2c78`](#insn-00aa2c78) → [`00aa2c60`](#insn-00aa2c60)
  - `FALL_THROUGH` [`00aa2c78`](#insn-00aa2c78) → [`00aa2c7c`](#insn-00aa2c7c)
- ブロック [`00aa2c7c`](#insn-00aa2c7c) 範囲 `[['00aa2c7c', '00aa2c83']]`
  - `CONDITIONAL_JUMP` [`00aa2c80`](#insn-00aa2c80) → [`00aa2b74`](#insn-00aa2b74)
  - `FALL_THROUGH` [`00aa2c80`](#insn-00aa2c80) → [`00aa2c84`](#insn-00aa2c84)
- ブロック [`00aa2c84`](#insn-00aa2c84) 範囲 `[['00aa2c84', '00aa2c8b']]`
  - `CONDITIONAL_JUMP` [`00aa2c88`](#insn-00aa2c88) → [`00aa2c6c`](#insn-00aa2c6c)
  - `FALL_THROUGH` [`00aa2c88`](#insn-00aa2c88) → [`00aa2c8c`](#insn-00aa2c8c)
- ブロック [`00aa2c8c`](#insn-00aa2c8c) 範囲 `[['00aa2c8c', '00aa2c8f']]`
  - `FALL_THROUGH` [`00aa2c8c`](#insn-00aa2c8c) → [`00aa2c90`](#insn-00aa2c90)
- ブロック [`00aa2c90`](#insn-00aa2c90) 範囲 `[['00aa2c90', '00aa2cc3']]`
  - `CONDITIONAL_JUMP` [`00aa2cc0`](#insn-00aa2cc0) → [`00aa2b60`](#insn-00aa2b60)
  - `FALL_THROUGH` [`00aa2cc0`](#insn-00aa2cc0) → [`00aa2cc4`](#insn-00aa2cc4)
- ブロック [`00aa2cc4`](#insn-00aa2cc4) 範囲 `[['00aa2cc4', '00aa2ccf']]`
  - `UNCONDITIONAL_JUMP` [`00aa2ccc`](#insn-00aa2ccc) → [`00aa2b60`](#insn-00aa2b60)
- ブロック [`00aa2cd0`](#insn-00aa2cd0) 範囲 `[['00aa2cd0', '00aa2cef']]`

## 命令位置別の参照

- [`00aa2b00`](#insn-00aa2b00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b04`](#insn-00aa2b04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b08`](#insn-00aa2b08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b0c`](#insn-00aa2b0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b10`](#insn-00aa2b10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b14`](#insn-00aa2b14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b34`](#insn-00aa2b34) → [`0086be6c`](../0086b/0086be6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086be6c` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b44`](#insn-00aa2b44) → [`00480178`](../00480/00480178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480178` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b50`](#insn-00aa2b50) → `Stack[-0x64]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b54`](#insn-00aa2b54) → [`00aa2cd0`](#insn-00aa2cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b5c`](#insn-00aa2b5c) → [`00aa2b8c`](#insn-00aa2b8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b64`](#insn-00aa2b64) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b74`](#insn-00aa2b74) → `Stack[-0x64]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b88`](#insn-00aa2b88) → [`00aa2cd0`](#insn-00aa2cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b90`](#insn-00aa2b90) → [`004801d8`](../00480/004801d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004801d8` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b9c`](#insn-00aa2b9c) → [`00480118`](../00480/00480118.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480118` · 推定シンボル `None` · 推定型 `None`
- [`00aa2bb0`](#insn-00aa2bb0) → [`00aa2bc4`](#insn-00aa2bc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2bb4`](#insn-00aa2bb4) → [`00aa2be8`](#insn-00aa2be8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2bc0`](#insn-00aa2bc0) → [`00aa2be8`](#insn-00aa2be8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2bd0`](#insn-00aa2bd0) → [`00aa2bb8`](#insn-00aa2bb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2bd8`](#insn-00aa2bd8) → [`00aa2c38`](#insn-00aa2c38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2be0`](#insn-00aa2be0) → [`00aa2bc4`](#insn-00aa2bc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2bf0`](#insn-00aa2bf0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c18`](#insn-00aa2c18) → [`00aa2c24`](#insn-00aa2c24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c28`](#insn-00aa2c28) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c44`](#insn-00aa2c44) → [`00480118`](../00480/00480118.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480118` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c58`](#insn-00aa2c58) → [`00aa2c6c`](#insn-00aa2c6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c5c`](#insn-00aa2c5c) → [`00aa2c90`](#insn-00aa2c90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c68`](#insn-00aa2c68) → [`00aa2c90`](#insn-00aa2c90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c78`](#insn-00aa2c78) → [`00aa2c60`](#insn-00aa2c60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c80`](#insn-00aa2c80) → [`00aa2b74`](#insn-00aa2b74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c88`](#insn-00aa2c88) → [`00aa2c6c`](#insn-00aa2c6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c98`](#insn-00aa2c98) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cc0`](#insn-00aa2cc0) → [`00aa2b60`](#insn-00aa2b60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2ccc`](#insn-00aa2ccc) → [`00aa2b60`](#insn-00aa2b60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cd0`](#insn-00aa2cd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cd4`](#insn-00aa2cd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cd8`](#insn-00aa2cd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cdc`](#insn-00aa2cdc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2ce0`](#insn-00aa2ce0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2ce4`](#insn-00aa2ce4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa2b00`](#insn-00aa2b00)

~~~json
{
  "source": "00aa2b00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b04`](#insn-00aa2b04)

~~~json
{
  "source": "00aa2b04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b08`](#insn-00aa2b08)

~~~json
{
  "source": "00aa2b08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b0c`](#insn-00aa2b0c)

~~~json
{
  "source": "00aa2b0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b10`](#insn-00aa2b10)

~~~json
{
  "source": "00aa2b10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b14`](#insn-00aa2b14)

~~~json
{
  "source": "00aa2b14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b34`](#insn-00aa2b34)

~~~json
{
  "source": "00aa2b34",
  "target": "0086be6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2b44`](#insn-00aa2b44)

~~~json
{
  "source": "00aa2b44",
  "target": "00480178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2b50`](#insn-00aa2b50)

~~~json
{
  "source": "00aa2b50",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b54`](#insn-00aa2b54)

~~~json
{
  "source": "00aa2b54",
  "target": "00aa2cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b5c`](#insn-00aa2b5c)

~~~json
{
  "source": "00aa2b5c",
  "target": "00aa2b8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b64`](#insn-00aa2b64)

~~~json
{
  "source": "00aa2b64",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2b74`](#insn-00aa2b74)

~~~json
{
  "source": "00aa2b74",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b88`](#insn-00aa2b88)

~~~json
{
  "source": "00aa2b88",
  "target": "00aa2cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b90`](#insn-00aa2b90)

~~~json
{
  "source": "00aa2b90",
  "target": "004801d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2b9c`](#insn-00aa2b9c)

~~~json
{
  "source": "00aa2b9c",
  "target": "00480118",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2bb0`](#insn-00aa2bb0)

~~~json
{
  "source": "00aa2bb0",
  "target": "00aa2bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2bb4`](#insn-00aa2bb4)

~~~json
{
  "source": "00aa2bb4",
  "target": "00aa2be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2bc0`](#insn-00aa2bc0)

~~~json
{
  "source": "00aa2bc0",
  "target": "00aa2be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2bd0`](#insn-00aa2bd0)

~~~json
{
  "source": "00aa2bd0",
  "target": "00aa2bb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2bd8`](#insn-00aa2bd8)

~~~json
{
  "source": "00aa2bd8",
  "target": "00aa2c38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2be0`](#insn-00aa2be0)

~~~json
{
  "source": "00aa2be0",
  "target": "00aa2bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2bf0`](#insn-00aa2bf0)

~~~json
{
  "source": "00aa2bf0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2c18`](#insn-00aa2c18)

~~~json
{
  "source": "00aa2c18",
  "target": "00aa2c24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c28`](#insn-00aa2c28)

~~~json
{
  "source": "00aa2c28",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2c44`](#insn-00aa2c44)

~~~json
{
  "source": "00aa2c44",
  "target": "00480118",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2c58`](#insn-00aa2c58)

~~~json
{
  "source": "00aa2c58",
  "target": "00aa2c6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c5c`](#insn-00aa2c5c)

~~~json
{
  "source": "00aa2c5c",
  "target": "00aa2c90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c68`](#insn-00aa2c68)

~~~json
{
  "source": "00aa2c68",
  "target": "00aa2c90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c78`](#insn-00aa2c78)

~~~json
{
  "source": "00aa2c78",
  "target": "00aa2c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c80`](#insn-00aa2c80)

~~~json
{
  "source": "00aa2c80",
  "target": "00aa2b74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c88`](#insn-00aa2c88)

~~~json
{
  "source": "00aa2c88",
  "target": "00aa2c6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c98`](#insn-00aa2c98)

~~~json
{
  "source": "00aa2c98",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2cc0`](#insn-00aa2cc0)

~~~json
{
  "source": "00aa2cc0",
  "target": "00aa2b60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2ccc`](#insn-00aa2ccc)

~~~json
{
  "source": "00aa2ccc",
  "target": "00aa2b60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cd0`](#insn-00aa2cd0)

~~~json
{
  "source": "00aa2cd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cd4`](#insn-00aa2cd4)

~~~json
{
  "source": "00aa2cd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cd8`](#insn-00aa2cd8)

~~~json
{
  "source": "00aa2cd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cdc`](#insn-00aa2cdc)

~~~json
{
  "source": "00aa2cdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2ce0`](#insn-00aa2ce0)

~~~json
{
  "source": "00aa2ce0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2ce4`](#insn-00aa2ce4)

~~~json
{
  "source": "00aa2ce4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
