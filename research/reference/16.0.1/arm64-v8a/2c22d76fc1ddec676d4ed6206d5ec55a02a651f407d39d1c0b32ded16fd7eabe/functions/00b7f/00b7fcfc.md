# 00b7fcfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b7f8d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f8d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-abd4801346ad865fef406be0f8d7544e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b7fd98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-b4018aa58a3f241135db9a91fb961793)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7fcfc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm",
  "size": 320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "526006b91b89406afc295c7d8c7af69d6ee7ee30e9fa9551bb5e303c623eb7fa",
  "source_text_sha256": "526006b91b89406afc295c7d8c7af69d6ee7ee30e9fa9551bb5e303c623eb7fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7fcfc",
        "00b7fe3b"
      ]
    ],
    "bytes_sha256": "43a3fd398ad8e8e8a0b23ce30a8cab933bcceb1bcfd433a965751cee1c992b8f",
    "instruction_count": 80,
    "instruction_bytes": 320,
    "body_bytes": 320,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c280](../00c5c/00c5c280.md)

## 呼び出し先

- [00c5c1a0](../00c5c/00c5c1a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2062 bytes

~~~c

void _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm
               (long param_1,long param_2,long param_3,ulong param_4)

{
  ulong uVar1;
  int iVar2;
  uint uVar3;
  ulong uVar4;
  long lVar5;
  
  param_3 = param_3 * param_2;
  *(undefined1 *)(param_1 + 0x60) = 1;
  if (param_3 != 0) {
    if (*(ulong *)(param_1 + 0x68) < 4) {
      *(undefined8 *)(param_1 + 0x68) = 4;
    }
    iVar2 = *(int *)(param_1 + 0x30);
    uVar3 = -((int)param_3 + iVar2);
    uVar1 = (ulong)uVar3 & 3;
    if ((uVar3 & 3) != 0) {
      lVar5 = *(long *)(param_1 + 0x40);
      if ((uint)((int)lVar5 - *(int *)(param_1 + 0x48)) < uVar1) {
        _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar1);
        lVar5 = *(long *)(param_1 + 0x40);
        iVar2 = *(int *)(param_1 + 0x30);
      }
      *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar5 - uVar1);
      *(int *)(param_1 + 0x30) = iVar2 + (int)uVar1;
      *(undefined1 *)(lVar5 - uVar1) = 0;
      if (uVar1 != 1) {
        uVar4 = 1;
        do {
          *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar4) = 0;
          uVar4 = uVar4 + 1;
        } while (uVar1 != uVar4);
      }
    }
    if (*(ulong *)(param_1 + 0x68) < param_4) {
      *(ulong *)(param_1 + 0x68) = param_4;
    }
    uVar3 = *(uint *)(param_1 + 0x30);
    uVar1 = param_4 - 1 & -(param_3 + (ulong)uVar3);
    if (uVar1 != 0) {
      lVar5 = *(long *)(param_1 + 0x40);
      if ((uint)((int)lVar5 - *(int *)(param_1 + 0x48)) < uVar1) {
        _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar1);
        lVar5 = *(long *)(param_1 + 0x40);
        uVar3 = *(uint *)(param_1 + 0x30);
      }
      *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar5 - uVar1);
      *(uint *)(param_1 + 0x30) = uVar3 + (int)uVar1;
      *(undefined1 *)(lVar5 - uVar1) = 0;
      if (uVar1 != 1) {
        uVar4 = 1;
        do {
          *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar4) = 0;
          uVar4 = uVar4 + 1;
        } while (uVar1 != uVar4);
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7fcfc"></a> `00b7fcfc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b7fd00"></a> `00b7fd00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7fd04"></a> `00b7fd04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7fd08"></a> `00b7fd08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b7fd0c"></a> `00b7fd0c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fd10"></a> `00b7fd10` | `56 7c 01 9b` | mul x22,x2,x1 | `FALL_THROUGH`
<a id="insn-00b7fd14"></a> `00b7fd14` | `08 80 01 39` | strb w8,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00b7fd18"></a> `00b7fd18` | `b6 08 00 b4` | cbz x22,0x00b7fe2c | `CONDITIONAL_JUMP`
<a id="insn-00b7fd1c"></a> `00b7fd1c` | `08 34 40 f9` | ldr x8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00b7fd20"></a> `00b7fd20` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00b7fd24"></a> `00b7fd24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7fd28"></a> `00b7fd28` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b7fd2c"></a> `00b7fd2c` | `68 00 00 54` | b.hi 0x00b7fd38 | `CONDITIONAL_JUMP`
<a id="insn-00b7fd30"></a> `00b7fd30` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00b7fd34"></a> `00b7fd34` | `68 36 00 f9` | str x8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b7fd38"></a> `00b7fd38` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7fd3c"></a> `00b7fd3c` | `c9 02 08 0b` | add w9,w22,w8 | `FALL_THROUGH`
<a id="insn-00b7fd40"></a> `00b7fd40` | `e9 03 09 4b` | neg w9,w9 | `FALL_THROUGH`
<a id="insn-00b7fd44"></a> `00b7fd44` | `35 05 40 f2` | ands x21,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00b7fd48"></a> `00b7fd48` | `00 03 00 54` | b.eq 0x00b7fda8 | `CONDITIONAL_JUMP`
<a id="insn-00b7fd4c"></a> `00b7fd4c` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fd50"></a> `00b7fd50` | `6a 4a 40 b9` | ldr w10,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7fd54"></a> `00b7fd54` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00b7fd58"></a> `00b7fd58` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00b7fd5c"></a> `00b7fd5c` | `c2 00 00 54` | b.cs 0x00b7fd74 | `CONDITIONAL_JUMP`
<a id="insn-00b7fd60"></a> `00b7fd60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7fd64"></a> `00b7fd64` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b7fd68"></a> `00b7fd68` | `0e 71 03 94` | bl 0x00c5c1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fd6c"></a> `00b7fd6c` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fd70"></a> `00b7fd70` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7fd74"></a> `00b7fd74` | `29 01 15 cb` | sub x9,x9,x21 | `FALL_THROUGH`
<a id="insn-00b7fd78"></a> `00b7fd78` | `08 01 15 0b` | add w8,w8,w21 | `FALL_THROUGH`
<a id="insn-00b7fd7c"></a> `00b7fd7c` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fd80"></a> `00b7fd80` | `69 22 00 f9` | str x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fd84"></a> `00b7fd84` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7fd88"></a> `00b7fd88` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b7fd8c"></a> `00b7fd8c` | `e0 00 00 54` | b.eq 0x00b7fda8 | `CONDITIONAL_JUMP`
<a id="insn-00b7fd90"></a> `00b7fd90` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fd94"></a> `00b7fd94` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fd98"></a> `00b7fd98` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b7fd9c"></a> `00b7fd9c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fda0"></a> `00b7fda0` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00b7fda4"></a> `00b7fda4` | `81 ff ff 54` | b.ne 0x00b7fd94 | `CONDITIONAL_JUMP`
<a id="insn-00b7fda8"></a> `00b7fda8` | `68 36 40 f9` | ldr x8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b7fdac"></a> `00b7fdac` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00b7fdb0"></a> `00b7fdb0` | `42 00 00 54` | b.cs 0x00b7fdb8 | `CONDITIONAL_JUMP`
<a id="insn-00b7fdb4"></a> `00b7fdb4` | `74 36 00 f9` | str x20,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b7fdb8"></a> `00b7fdb8` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7fdbc"></a> `00b7fdbc` | `8a 06 00 d1` | sub x10,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fdc0"></a> `00b7fdc0` | `c9 02 08 8b` | add x9,x22,x8 | `FALL_THROUGH`
<a id="insn-00b7fdc4"></a> `00b7fdc4` | `e9 03 09 cb` | neg x9,x9 | `FALL_THROUGH`
<a id="insn-00b7fdc8"></a> `00b7fdc8` | `54 01 09 ea` | ands x20,x10,x9 | `FALL_THROUGH`
<a id="insn-00b7fdcc"></a> `00b7fdcc` | `00 03 00 54` | b.eq 0x00b7fe2c | `CONDITIONAL_JUMP`
<a id="insn-00b7fdd0"></a> `00b7fdd0` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fdd4"></a> `00b7fdd4` | `6a 4a 40 b9` | ldr w10,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7fdd8"></a> `00b7fdd8` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00b7fddc"></a> `00b7fddc` | `5f 01 14 eb` | cmp x10,x20 | `FALL_THROUGH`
<a id="insn-00b7fde0"></a> `00b7fde0` | `c2 00 00 54` | b.cs 0x00b7fdf8 | `CONDITIONAL_JUMP`
<a id="insn-00b7fde4"></a> `00b7fde4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7fde8"></a> `00b7fde8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b7fdec"></a> `00b7fdec` | `ed 70 03 94` | bl 0x00c5c1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fdf0"></a> `00b7fdf0` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fdf4"></a> `00b7fdf4` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7fdf8"></a> `00b7fdf8` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00b7fdfc"></a> `00b7fdfc` | `08 01 14 0b` | add w8,w8,w20 | `FALL_THROUGH`
<a id="insn-00b7fe00"></a> `00b7fe00` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fe04"></a> `00b7fe04` | `69 22 00 f9` | str x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fe08"></a> `00b7fe08` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7fe0c"></a> `00b7fe0c` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b7fe10"></a> `00b7fe10` | `e0 00 00 54` | b.eq 0x00b7fe2c | `CONDITIONAL_JUMP`
<a id="insn-00b7fe14"></a> `00b7fe14` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fe18"></a> `00b7fe18` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7fe1c"></a> `00b7fe1c` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b7fe20"></a> `00b7fe20` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7fe24"></a> `00b7fe24` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00b7fe28"></a> `00b7fe28` | `81 ff ff 54` | b.ne 0x00b7fe18 | `CONDITIONAL_JUMP`
<a id="insn-00b7fe2c"></a> `00b7fe2c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7fe30"></a> `00b7fe30` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7fe34"></a> `00b7fe34` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b7fe38"></a> `00b7fe38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7fcfc`](#insn-00b7fcfc) 範囲 `[['00b7fcfc', '00b7fd1b']]`
  - `CONDITIONAL_JUMP` [`00b7fd18`](#insn-00b7fd18) → [`00b7fe2c`](#insn-00b7fe2c)
  - `FALL_THROUGH` [`00b7fd18`](#insn-00b7fd18) → [`00b7fd1c`](#insn-00b7fd1c)
- ブロック [`00b7fd1c`](#insn-00b7fd1c) 範囲 `[['00b7fd1c', '00b7fd2f']]`
  - `CONDITIONAL_JUMP` [`00b7fd2c`](#insn-00b7fd2c) → [`00b7fd38`](#insn-00b7fd38)
  - `FALL_THROUGH` [`00b7fd2c`](#insn-00b7fd2c) → [`00b7fd30`](#insn-00b7fd30)
- ブロック [`00b7fd30`](#insn-00b7fd30) 範囲 `[['00b7fd30', '00b7fd37']]`
  - `FALL_THROUGH` [`00b7fd34`](#insn-00b7fd34) → [`00b7fd38`](#insn-00b7fd38)
- ブロック [`00b7fd38`](#insn-00b7fd38) 範囲 `[['00b7fd38', '00b7fd4b']]`
  - `CONDITIONAL_JUMP` [`00b7fd48`](#insn-00b7fd48) → [`00b7fda8`](#insn-00b7fda8)
  - `FALL_THROUGH` [`00b7fd48`](#insn-00b7fd48) → [`00b7fd4c`](#insn-00b7fd4c)
- ブロック [`00b7fd4c`](#insn-00b7fd4c) 範囲 `[['00b7fd4c', '00b7fd5f']]`
  - `CONDITIONAL_JUMP` [`00b7fd5c`](#insn-00b7fd5c) → [`00b7fd74`](#insn-00b7fd74)
  - `FALL_THROUGH` [`00b7fd5c`](#insn-00b7fd5c) → [`00b7fd60`](#insn-00b7fd60)
- ブロック [`00b7fd60`](#insn-00b7fd60) 範囲 `[['00b7fd60', '00b7fd73']]`
  - `FALL_THROUGH` [`00b7fd70`](#insn-00b7fd70) → [`00b7fd74`](#insn-00b7fd74)
- ブロック [`00b7fd74`](#insn-00b7fd74) 範囲 `[['00b7fd74', '00b7fd8f']]`
  - `CONDITIONAL_JUMP` [`00b7fd8c`](#insn-00b7fd8c) → [`00b7fda8`](#insn-00b7fda8)
  - `FALL_THROUGH` [`00b7fd8c`](#insn-00b7fd8c) → [`00b7fd90`](#insn-00b7fd90)
- ブロック [`00b7fd90`](#insn-00b7fd90) 範囲 `[['00b7fd90', '00b7fd93']]`
  - `FALL_THROUGH` [`00b7fd90`](#insn-00b7fd90) → [`00b7fd94`](#insn-00b7fd94)
- ブロック [`00b7fd94`](#insn-00b7fd94) 範囲 `[['00b7fd94', '00b7fda7']]`
  - `CONDITIONAL_JUMP` [`00b7fda4`](#insn-00b7fda4) → [`00b7fd94`](#insn-00b7fd94)
  - `FALL_THROUGH` [`00b7fda4`](#insn-00b7fda4) → [`00b7fda8`](#insn-00b7fda8)
- ブロック [`00b7fda8`](#insn-00b7fda8) 範囲 `[['00b7fda8', '00b7fdb3']]`
  - `CONDITIONAL_JUMP` [`00b7fdb0`](#insn-00b7fdb0) → [`00b7fdb8`](#insn-00b7fdb8)
  - `FALL_THROUGH` [`00b7fdb0`](#insn-00b7fdb0) → [`00b7fdb4`](#insn-00b7fdb4)
- ブロック [`00b7fdb4`](#insn-00b7fdb4) 範囲 `[['00b7fdb4', '00b7fdb7']]`
  - `FALL_THROUGH` [`00b7fdb4`](#insn-00b7fdb4) → [`00b7fdb8`](#insn-00b7fdb8)
- ブロック [`00b7fdb8`](#insn-00b7fdb8) 範囲 `[['00b7fdb8', '00b7fdcf']]`
  - `CONDITIONAL_JUMP` [`00b7fdcc`](#insn-00b7fdcc) → [`00b7fe2c`](#insn-00b7fe2c)
  - `FALL_THROUGH` [`00b7fdcc`](#insn-00b7fdcc) → [`00b7fdd0`](#insn-00b7fdd0)
- ブロック [`00b7fdd0`](#insn-00b7fdd0) 範囲 `[['00b7fdd0', '00b7fde3']]`
  - `CONDITIONAL_JUMP` [`00b7fde0`](#insn-00b7fde0) → [`00b7fdf8`](#insn-00b7fdf8)
  - `FALL_THROUGH` [`00b7fde0`](#insn-00b7fde0) → [`00b7fde4`](#insn-00b7fde4)
- ブロック [`00b7fde4`](#insn-00b7fde4) 範囲 `[['00b7fde4', '00b7fdf7']]`
  - `FALL_THROUGH` [`00b7fdf4`](#insn-00b7fdf4) → [`00b7fdf8`](#insn-00b7fdf8)
- ブロック [`00b7fdf8`](#insn-00b7fdf8) 範囲 `[['00b7fdf8', '00b7fe13']]`
  - `CONDITIONAL_JUMP` [`00b7fe10`](#insn-00b7fe10) → [`00b7fe2c`](#insn-00b7fe2c)
  - `FALL_THROUGH` [`00b7fe10`](#insn-00b7fe10) → [`00b7fe14`](#insn-00b7fe14)
- ブロック [`00b7fe14`](#insn-00b7fe14) 範囲 `[['00b7fe14', '00b7fe17']]`
  - `FALL_THROUGH` [`00b7fe14`](#insn-00b7fe14) → [`00b7fe18`](#insn-00b7fe18)
- ブロック [`00b7fe18`](#insn-00b7fe18) 範囲 `[['00b7fe18', '00b7fe2b']]`
  - `CONDITIONAL_JUMP` [`00b7fe28`](#insn-00b7fe28) → [`00b7fe18`](#insn-00b7fe18)
  - `FALL_THROUGH` [`00b7fe28`](#insn-00b7fe28) → [`00b7fe2c`](#insn-00b7fe2c)
- ブロック [`00b7fe2c`](#insn-00b7fe2c) 範囲 `[['00b7fe2c', '00b7fe3b']]`

## 命令位置別の参照

- [`00b7fcfc`](#insn-00b7fcfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd00`](#insn-00b7fd00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd04`](#insn-00b7fd04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd18`](#insn-00b7fd18) → [`00b7fe2c`](#insn-00b7fe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd2c`](#insn-00b7fd2c) → [`00b7fd38`](#insn-00b7fd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd48`](#insn-00b7fd48) → [`00b7fda8`](#insn-00b7fda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd5c`](#insn-00b7fd5c) → [`00b7fd74`](#insn-00b7fd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd68`](#insn-00b7fd68) → [`00c5c1a0`](../00c5c/00c5c1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd8c`](#insn-00b7fd8c) → [`00b7fda8`](#insn-00b7fda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fda4`](#insn-00b7fda4) → [`00b7fd94`](#insn-00b7fd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fdb0`](#insn-00b7fdb0) → [`00b7fdb8`](#insn-00b7fdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fdcc`](#insn-00b7fdcc) → [`00b7fe2c`](#insn-00b7fe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fde0`](#insn-00b7fde0) → [`00b7fdf8`](#insn-00b7fdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fdec`](#insn-00b7fdec) → [`00c5c1a0`](../00c5c/00c5c1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7fe10`](#insn-00b7fe10) → [`00b7fe2c`](#insn-00b7fe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fe28`](#insn-00b7fe28) → [`00b7fe18`](#insn-00b7fe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fe2c`](#insn-00b7fe2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fe30`](#insn-00b7fe30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7fcfc`](#insn-00b7fcfc)

~~~json
{
  "source": "00b7fcfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd00`](#insn-00b7fd00)

~~~json
{
  "source": "00b7fd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd04`](#insn-00b7fd04)

~~~json
{
  "source": "00b7fd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd18`](#insn-00b7fd18)

~~~json
{
  "source": "00b7fd18",
  "target": "00b7fe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd2c`](#insn-00b7fd2c)

~~~json
{
  "source": "00b7fd2c",
  "target": "00b7fd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd48`](#insn-00b7fd48)

~~~json
{
  "source": "00b7fd48",
  "target": "00b7fda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd5c`](#insn-00b7fd5c)

~~~json
{
  "source": "00b7fd5c",
  "target": "00b7fd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd68`](#insn-00b7fd68)

~~~json
{
  "source": "00b7fd68",
  "target": "00c5c1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fd8c`](#insn-00b7fd8c)

~~~json
{
  "source": "00b7fd8c",
  "target": "00b7fda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fda4`](#insn-00b7fda4)

~~~json
{
  "source": "00b7fda4",
  "target": "00b7fd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fdb0`](#insn-00b7fdb0)

~~~json
{
  "source": "00b7fdb0",
  "target": "00b7fdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fdcc`](#insn-00b7fdcc)

~~~json
{
  "source": "00b7fdcc",
  "target": "00b7fe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fde0`](#insn-00b7fde0)

~~~json
{
  "source": "00b7fde0",
  "target": "00b7fdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fdec`](#insn-00b7fdec)

~~~json
{
  "source": "00b7fdec",
  "target": "00c5c1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fe10`](#insn-00b7fe10)

~~~json
{
  "source": "00b7fe10",
  "target": "00b7fe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fe28`](#insn-00b7fe28)

~~~json
{
  "source": "00b7fe28",
  "target": "00b7fe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fe2c`](#insn-00b7fe2c)

~~~json
{
  "source": "00b7fe2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fe30`](#insn-00b7fe30)

~~~json
{
  "source": "00b7fe30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
