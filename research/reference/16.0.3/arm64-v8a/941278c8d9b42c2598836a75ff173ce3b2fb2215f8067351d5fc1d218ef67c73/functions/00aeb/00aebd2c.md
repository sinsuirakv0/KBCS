# 00aebd2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aead38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aead38.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0011.md#compare-00d0cabd47b105e53f079048d9123f8c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebd2c",
  "name": "FUN_00aebd2c",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9434a30280d9c0933cad1a670cc1389ae15f9f949169d4c10e5e1baf07b3776a",
  "source_text_sha256": "9434a30280d9c0933cad1a670cc1389ae15f9f949169d4c10e5e1baf07b3776a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebd2c",
        "00aebe7f"
      ]
    ],
    "bytes_sha256": "a1198dd2d1dec63d91ee21cf1a0ad8f16e3c1ff3620ed8cc23b0e50e2a2e6d0c",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007fc1ec](../007fc/007fc1ec.md)
- [0099803c](../00998/0099803c.md)
- [009fe62c](../009fe/009fe62c.md)
- [00a0177c](../00a01/00a0177c.md)
- [00a032d8](../00a03/00a032d8.md)
- [00a04e68](../00a04/00a04e68.md)
- [00ae231c](../00ae2/00ae231c.md)

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [00467e8c](../00467/00467e8c.md)
- [004682b4](../00468/004682b4.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [008524fc](../00852/008524fc.md)
- [00a83a34](../00a83/00a83a34.md)
- [00a845ec](../00a84/00a845ec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1310 bytes

~~~c

void FUN_00aebd2c(long param_1,int param_2)

{
  int iVar1;
  int iVar2;
  int iVar3;
  undefined8 uVar4;
  long lVar5;
  
  iVar2 = FUN_00a83a34(param_1 + 0x3078,0x65);
  uVar4 = FUN_00467bc0();
                    /* try { // try from 00aebd60 to 00bebd6b has its CatchHandler @ 00aebecc */
  FUN_008524fc();
  iVar3 = FUN_0046cde4();
                    /* try { // try from 00aebd6c to 00bebe97 has its CatchHandler @ 00aeb974 */
  iVar2 = iVar2 * 0x27;
  lVar5 = FUN_008524fc();
  if (param_2 == 0) {
    iVar1 = iVar2;
    if (iVar2 < 0) {
      iVar1 = iVar2 + 1;
    }
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    param_2 = (((iVar3 >> 1) - (iVar1 >> 1)) -
              *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5)) + 0x12;
  }
  else {
    iVar3 = iVar2 + 0x18;
    if (-0x18 < iVar2) {
      iVar3 = iVar2 + 0x17;
    }
    param_2 = param_2 - (iVar3 >> 1);
  }
  FUN_00467e8c(uVar4,0xff,0xff,0xff,0xe6);
  iVar3 = FUN_0046cd24(param_1);
  FUN_004682b4(uVar4,(int)((double)iVar3 * 0.5 + -430.0),param_2,0x35c,iVar2 + 0x17);
  FUN_00467e8c(uVar4,0,0,0,0xff);
  iVar3 = FUN_0046cd24(param_1);
  if (iVar3 < 0) {
    iVar3 = iVar3 + 1;
  }
  FUN_00a845ec(0x3f800000,param_1 + 0x3078,0x65,iVar3 >> 1,param_2 + 0xd,1);
  FUN_00467e8c(uVar4,0xff,0xff,0xff,0xff);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebd2c"></a> `00aebd2c` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aebd30"></a> `00aebd30` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebd34"></a> `00aebd34` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebd38"></a> `00aebd38` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aebd3c"></a> `00aebd3c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aebd40"></a> `00aebd40` | `17 0f 86 52` | mov w23,#0x3078 | `FALL_THROUGH`
<a id="insn-00aebd44"></a> `00aebd44` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00aebd48"></a> `00aebd48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebd4c"></a> `00aebd4c` | `00 00 17 8b` | add x0,x0,x23 | `FALL_THROUGH`
<a id="insn-00aebd50"></a> `00aebd50` | `a1 0c 80 52` | mov w1,#0x65 | `FALL_THROUGH`
<a id="insn-00aebd54"></a> `00aebd54` | `38 5f fe 97` | bl 0x00a83a34 | `UNCONDITIONAL_CALL`
<a id="insn-00aebd58"></a> `00aebd58` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aebd5c"></a> `00aebd5c` | `99 ef e5 97` | bl 0x00467bc0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebd60"></a> `00aebd60` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aebd64"></a> `00aebd64` | `e6 99 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aebd68"></a> `00aebd68` | `1f 04 e6 97` | bl 0x0046cde4 | `UNCONDITIONAL_CALL`
<a id="insn-00aebd6c"></a> `00aebd6c` | `e8 04 80 52` | mov w8,#0x27 | `FALL_THROUGH`
<a id="insn-00aebd70"></a> `00aebd70` | `d8 7e 08 1b` | mul w24,w22,w8 | `FALL_THROUGH`
<a id="insn-00aebd74"></a> `00aebd74` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aebd78"></a> `00aebd78` | `e1 99 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aebd7c"></a> `00aebd7c` | `d5 00 00 34` | cbz w21,0x00aebd94 | `CONDITIONAL_JUMP`
<a id="insn-00aebd80"></a> `00aebd80` | `16 5f 00 31` | adds w22,w24,#0x17 | `FALL_THROUGH`
<a id="insn-00aebd84"></a> `00aebd84` | `08 63 00 11` | add w8,w24,#0x18 | `FALL_THROUGH`
<a id="insn-00aebd88"></a> `00aebd88` | `08 b1 96 1a` | csel w8,w8,w22,lt | `FALL_THROUGH`
<a id="insn-00aebd8c"></a> `00aebd8c` | `b5 06 88 4b` | sub w21,w21,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aebd90"></a> `00aebd90` | `0d 00 00 14` | b 0x00aebdc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aebd94"></a> `00aebd94` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-00aebd98"></a> `00aebd98` | `0a 3d 87 52` | mov w10,#0x39e8 | `FALL_THROUGH`
<a id="insn-00aebd9c"></a> `00aebd9c` | `08 a7 98 1a` | cinc w8,w24,lt | `FALL_THROUGH`
<a id="insn-00aebda0"></a> `00aebda0` | `df 02 00 71` | cmp w22,#0x0 | `FALL_THROUGH`
<a id="insn-00aebda4"></a> `00aebda4` | `6a 06 a0 72` | movk w10,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aebda8"></a> `00aebda8` | `c9 a6 96 1a` | cinc w9,w22,lt | `FALL_THROUGH`
<a id="insn-00aebdac"></a> `00aebdac` | `16 5f 00 11` | add w22,w24,#0x17 | `FALL_THROUGH`
<a id="insn-00aebdb0"></a> `00aebdb0` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aebdb4"></a> `00aebdb4` | `28 05 88 4b` | sub w8,w9,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aebdb8"></a> `00aebdb8` | `09 68 6a b8` | ldr w9,[x0, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aebdbc"></a> `00aebdbc` | `08 01 09 4b` | sub w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aebdc0"></a> `00aebdc0` | `15 49 00 11` | add w21,w8,#0x12 | `FALL_THROUGH`
<a id="insn-00aebdc4"></a> `00aebdc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aebdc8"></a> `00aebdc8` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aebdcc"></a> `00aebdcc` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aebdd0"></a> `00aebdd0` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aebdd4"></a> `00aebdd4` | `c4 1c 80 52` | mov w4,#0xe6 | `FALL_THROUGH`
<a id="insn-00aebdd8"></a> `00aebdd8` | `2d f0 e5 97` | bl 0x00467e8c | `UNCONDITIONAL_CALL`
<a id="insn-00aebddc"></a> `00aebddc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebde0"></a> `00aebde0` | `d1 03 e6 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-00aebde4"></a> `00aebde4` | `08 00 dc d2` | mov x8,#0xe00000000000 | `FALL_THROUGH`
<a id="insn-00aebde8"></a> `00aebde8` | `00 00 62 1e` | scvtf d0,w0 | `FALL_THROUGH`
<a id="insn-00aebdec"></a> `00aebdec` | `01 10 6c 1e` | fmov d1,0x3fe0000000000000 | `FALL_THROUGH`
<a id="insn-00aebdf0"></a> `00aebdf0` | `48 0f f8 f2` | movk x8,#0xc07a, LSL #48 | `FALL_THROUGH`
<a id="insn-00aebdf4"></a> `00aebdf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aebdf8"></a> `00aebdf8` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aebdfc"></a> `00aebdfc` | `02 01 67 9e` | fmov d2,x8 | `FALL_THROUGH`
<a id="insn-00aebe00"></a> `00aebe00` | `83 6b 80 52` | mov w3,#0x35c | `FALL_THROUGH`
<a id="insn-00aebe04"></a> `00aebe04` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00aebe08"></a> `00aebe08` | `00 08 41 1f` | fmadd d0,d0,d1,d2 | `FALL_THROUGH`
<a id="insn-00aebe0c"></a> `00aebe0c` | `01 00 78 1e` | fcvtzs w1,d0 | `FALL_THROUGH`
<a id="insn-00aebe10"></a> `00aebe10` | `29 f1 e5 97` | bl 0x004682b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe14"></a> `00aebe14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aebe18"></a> `00aebe18` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aebe1c"></a> `00aebe1c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aebe20"></a> `00aebe20` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aebe24"></a> `00aebe24` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aebe28"></a> `00aebe28` | `19 f0 e5 97` | bl 0x00467e8c | `UNCONDITIONAL_CALL`
<a id="insn-00aebe2c"></a> `00aebe2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebe30"></a> `00aebe30` | `bd 03 e6 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe34"></a> `00aebe34` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aebe38"></a> `00aebe38` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-00aebe3c"></a> `00aebe3c` | `a3 36 00 11` | add w3,w21,#0xd | `FALL_THROUGH`
<a id="insn-00aebe40"></a> `00aebe40` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-00aebe44"></a> `00aebe44` | `60 02 17 8b` | add x0,x19,x23 | `FALL_THROUGH`
<a id="insn-00aebe48"></a> `00aebe48` | `a1 0c 80 52` | mov w1,#0x65 | `FALL_THROUGH`
<a id="insn-00aebe4c"></a> `00aebe4c` | `02 7d 01 13` | asr w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aebe50"></a> `00aebe50` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00aebe54"></a> `00aebe54` | `e6 61 fe 97` | bl 0x00a845ec | `UNCONDITIONAL_CALL`
<a id="insn-00aebe58"></a> `00aebe58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aebe5c"></a> `00aebe5c` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aebe60"></a> `00aebe60` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aebe64"></a> `00aebe64` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aebe68"></a> `00aebe68` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aebe6c"></a> `00aebe6c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aebe70"></a> `00aebe70` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebe74"></a> `00aebe74` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe78"></a> `00aebe78` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aebe7c"></a> `00aebe7c` | `04 f0 e5 17` | b 0x00467e8c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebd2c`](#insn-00aebd2c) 範囲 `[['00aebd2c', '00aebd5f']]`
  - `FALL_THROUGH` [`00aebd5c`](#insn-00aebd5c) → [`00aebd60`](#insn-00aebd60)
- ブロック [`00aebd60`](#insn-00aebd60) 範囲 `[['00aebd60', '00aebd6b']]`
  - `FALL_THROUGH` [`00aebd68`](#insn-00aebd68) → [`00aebd6c`](#insn-00aebd6c)
- ブロック [`00aebd6c`](#insn-00aebd6c) 範囲 `[['00aebd6c', '00aebd7f']]`
  - `CONDITIONAL_JUMP` [`00aebd7c`](#insn-00aebd7c) → [`00aebd94`](#insn-00aebd94)
  - `FALL_THROUGH` [`00aebd7c`](#insn-00aebd7c) → [`00aebd80`](#insn-00aebd80)
- ブロック [`00aebd80`](#insn-00aebd80) 範囲 `[['00aebd80', '00aebd93']]`
  - `UNCONDITIONAL_JUMP` [`00aebd90`](#insn-00aebd90) → [`00aebdc4`](#insn-00aebdc4)
- ブロック [`00aebd94`](#insn-00aebd94) 範囲 `[['00aebd94', '00aebdc3']]`
  - `FALL_THROUGH` [`00aebdc0`](#insn-00aebdc0) → [`00aebdc4`](#insn-00aebdc4)
- ブロック [`00aebdc4`](#insn-00aebdc4) 範囲 `[['00aebdc4', '00aebe7f']]`

## 命令位置別の参照

- [`00aebd2c`](#insn-00aebd2c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd30`](#insn-00aebd30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd34`](#insn-00aebd34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd38`](#insn-00aebd38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd54`](#insn-00aebd54) → [`00a83a34`](../00a83/00a83a34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83a34` · 推定シンボル `None` · 推定型 `None`
- [`00aebd5c`](#insn-00aebd5c) → [`00467bc0`](../00467/00467bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467bc0` · 推定シンボル `None` · 推定型 `None`
- [`00aebd64`](#insn-00aebd64) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aebd68`](#insn-00aebd68) → [`0046cde4`](../0046c/0046cde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cde4` · 推定シンボル `None` · 推定型 `None`
- [`00aebd78`](#insn-00aebd78) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aebd7c`](#insn-00aebd7c) → [`00aebd94`](#insn-00aebd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd90`](#insn-00aebd90) → [`00aebdc4`](#insn-00aebdc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdb8`](#insn-00aebdb8) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aebdd8`](#insn-00aebdd8) → [`00467e8c`](../00467/00467e8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467e8c` · 推定シンボル `None` · 推定型 `None`
- [`00aebde0`](#insn-00aebde0) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`00aebe10`](#insn-00aebe10) → [`004682b4`](../00468/004682b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004682b4` · 推定シンボル `None` · 推定型 `None`
- [`00aebe28`](#insn-00aebe28) → [`00467e8c`](../00467/00467e8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467e8c` · 推定シンボル `None` · 推定型 `None`
- [`00aebe30`](#insn-00aebe30) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`00aebe54`](#insn-00aebe54) → [`00a845ec`](../00a84/00a845ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a845ec` · 推定シンボル `None` · 推定型 `None`
- [`00aebe6c`](#insn-00aebe6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe70`](#insn-00aebe70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe74`](#insn-00aebe74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe78`](#insn-00aebe78) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe7c`](#insn-00aebe7c) → [`00467e8c`](../00467/00467e8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467e8c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebd2c`](#insn-00aebd2c)

~~~json
{
  "source": "00aebd2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd30`](#insn-00aebd30)

~~~json
{
  "source": "00aebd30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd34`](#insn-00aebd34)

~~~json
{
  "source": "00aebd34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd38`](#insn-00aebd38)

~~~json
{
  "source": "00aebd38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd54`](#insn-00aebd54)

~~~json
{
  "source": "00aebd54",
  "target": "00a83a34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebd5c`](#insn-00aebd5c)

~~~json
{
  "source": "00aebd5c",
  "target": "00467bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebd64`](#insn-00aebd64)

~~~json
{
  "source": "00aebd64",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebd68`](#insn-00aebd68)

~~~json
{
  "source": "00aebd68",
  "target": "0046cde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebd78`](#insn-00aebd78)

~~~json
{
  "source": "00aebd78",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebd7c`](#insn-00aebd7c)

~~~json
{
  "source": "00aebd7c",
  "target": "00aebd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd90`](#insn-00aebd90)

~~~json
{
  "source": "00aebd90",
  "target": "00aebdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdb8`](#insn-00aebdb8)

~~~json
{
  "source": "00aebdb8",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c36a0094780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebdd8`](#insn-00aebdd8)

~~~json
{
  "source": "00aebdd8",
  "target": "00467e8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebde0`](#insn-00aebde0)

~~~json
{
  "source": "00aebde0",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe10`](#insn-00aebe10)

~~~json
{
  "source": "00aebe10",
  "target": "004682b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe28`](#insn-00aebe28)

~~~json
{
  "source": "00aebe28",
  "target": "00467e8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe30`](#insn-00aebe30)

~~~json
{
  "source": "00aebe30",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe54`](#insn-00aebe54)

~~~json
{
  "source": "00aebe54",
  "target": "00a845ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe6c`](#insn-00aebe6c)

~~~json
{
  "source": "00aebe6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe70`](#insn-00aebe70)

~~~json
{
  "source": "00aebe70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe74`](#insn-00aebe74)

~~~json
{
  "source": "00aebe74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe78`](#insn-00aebe78)

~~~json
{
  "source": "00aebe78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe7c`](#insn-00aebe7c)

~~~json
{
  "source": "00aebe7c",
  "target": "00467e8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
