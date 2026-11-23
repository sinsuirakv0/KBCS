# 00add5ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00add674`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add674.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-73bafbc61e1a307df37af7ca4b8edee9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00add5ac",
  "name": "FUN_00add5ac",
  "size": 352,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c93d520fb9bc97daaf39e72d074021de4d6133aa5f184fce848e76c6d819532f",
  "source_text_sha256": "c93d520fb9bc97daaf39e72d074021de4d6133aa5f184fce848e76c6d819532f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00add5ac",
        "00add70b"
      ]
    ],
    "bytes_sha256": "a95c02fe70115714d4773a1ec815dfcbdd75178c98fe7cebe58ede48dc52f2ba",
    "instruction_count": 88,
    "instruction_bytes": 352,
    "body_bytes": 352,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ade630](../00ade/00ade630.md)

## 呼び出し先

- [00464a64](../00464/00464a64.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1353 bytes

~~~c

void FUN_00add5ac(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  int iVar2;
  
  uVar1 = FUN_00464a64(param_2,0);
  *param_1 = uVar1;
  iVar2 = FUN_00464a64(param_2,1);
  *(bool *)(param_1 + 1) = iVar2 == 1;
  uVar1 = FUN_00464a64(param_2,3);
  param_1[2] = uVar1;
                    /* catch() { ... } // from try @ 00add490 with catch @ 00add5fc */
  uVar1 = FUN_00464a64(param_2,4);
  param_1[3] = uVar1;
  uVar1 = FUN_00464a64(param_2,5);
  param_1[4] = uVar1;
  uVar1 = FUN_00464a64(param_2,6);
  param_1[5] = uVar1;
  uVar1 = FUN_00464a64(param_2,7);
  param_1[6] = uVar1;
  uVar1 = FUN_00464a64(param_2,8);
  param_1[10] = uVar1;
  uVar1 = FUN_00464a64(param_2,9);
  param_1[0xb] = uVar1;
  uVar1 = FUN_00464a64(param_2,10);
  param_1[0xd] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xb);
  param_1[0xc] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xc);
  param_1[0xe] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xd);
  param_1[0xf] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xe);
  param_1[0x10] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xf);
  param_1[9] = uVar1;
  uVar1 = FUN_00464a64(param_2,0x10);
  param_1[7] = uVar1;
  uVar1 = FUN_00464a64(param_2,0x11);
  param_1[8] = uVar1;
  uVar1 = FUN_00464a64(param_2,2);
  param_1[0x11] = uVar1;
  iVar2 = FUN_00464a64(param_2,0x12);
  *(bool *)(param_1 + 0x12) = iVar2 != 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00add5ac"></a> `00add5ac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00add5b0"></a> `00add5b0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00add5b4"></a> `00add5b4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00add5b8"></a> `00add5b8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00add5bc"></a> `00add5bc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00add5c0"></a> `00add5c0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00add5c4"></a> `00add5c4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00add5c8"></a> `00add5c8` | `27 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add5cc"></a> `00add5cc` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-00add5d0"></a> `00add5d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add5d4"></a> `00add5d4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00add5d8"></a> `00add5d8` | `23 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add5dc"></a> `00add5dc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00add5e0"></a> `00add5e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add5e4"></a> `00add5e4` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00add5e8"></a> `00add5e8` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00add5ec"></a> `00add5ec` | `68 12 00 39` | strb w8,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00add5f0"></a> `00add5f0` | `1d 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add5f4"></a> `00add5f4` | `60 0a 00 b9` | str w0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00add5f8"></a> `00add5f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add5fc"></a> `00add5fc` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00add600"></a> `00add600` | `19 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add604"></a> `00add604` | `60 0e 00 b9` | str w0,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00add608"></a> `00add608` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add60c"></a> `00add60c` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00add610"></a> `00add610` | `15 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add614"></a> `00add614` | `60 12 00 b9` | str w0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00add618"></a> `00add618` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add61c"></a> `00add61c` | `c1 00 80 52` | mov w1,#0x6 | `FALL_THROUGH`
<a id="insn-00add620"></a> `00add620` | `11 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add624"></a> `00add624` | `60 16 00 b9` | str w0,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00add628"></a> `00add628` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add62c"></a> `00add62c` | `e1 00 80 52` | mov w1,#0x7 | `FALL_THROUGH`
<a id="insn-00add630"></a> `00add630` | `0d 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add634"></a> `00add634` | `60 1a 00 b9` | str w0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00add638"></a> `00add638` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add63c"></a> `00add63c` | `01 01 80 52` | mov w1,#0x8 | `FALL_THROUGH`
<a id="insn-00add640"></a> `00add640` | `09 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add644"></a> `00add644` | `60 2a 00 b9` | str w0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00add648"></a> `00add648` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add64c"></a> `00add64c` | `21 01 80 52` | mov w1,#0x9 | `FALL_THROUGH`
<a id="insn-00add650"></a> `00add650` | `05 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add654"></a> `00add654` | `60 2e 00 b9` | str w0,[x19, #0x2c] | `FALL_THROUGH`
<a id="insn-00add658"></a> `00add658` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add65c"></a> `00add65c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00add660"></a> `00add660` | `01 1d e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add664"></a> `00add664` | `60 36 00 b9` | str w0,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00add668"></a> `00add668` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add66c"></a> `00add66c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00add670"></a> `00add670` | `fd 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add674"></a> `00add674` | `60 32 00 b9` | str w0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00add678"></a> `00add678` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add67c"></a> `00add67c` | `81 01 80 52` | mov w1,#0xc | `FALL_THROUGH`
<a id="insn-00add680"></a> `00add680` | `f9 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add684"></a> `00add684` | `60 3a 00 b9` | str w0,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00add688"></a> `00add688` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add68c"></a> `00add68c` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-00add690"></a> `00add690` | `f5 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add694"></a> `00add694` | `60 3e 00 b9` | str w0,[x19, #0x3c] | `FALL_THROUGH`
<a id="insn-00add698"></a> `00add698` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add69c"></a> `00add69c` | `c1 01 80 52` | mov w1,#0xe | `FALL_THROUGH`
<a id="insn-00add6a0"></a> `00add6a0` | `f1 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add6a4"></a> `00add6a4` | `60 42 00 b9` | str w0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00add6a8"></a> `00add6a8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add6ac"></a> `00add6ac` | `e1 01 80 52` | mov w1,#0xf | `FALL_THROUGH`
<a id="insn-00add6b0"></a> `00add6b0` | `ed 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add6b4"></a> `00add6b4` | `60 26 00 b9` | str w0,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00add6b8"></a> `00add6b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add6bc"></a> `00add6bc` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-00add6c0"></a> `00add6c0` | `e9 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add6c4"></a> `00add6c4` | `60 1e 00 b9` | str w0,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00add6c8"></a> `00add6c8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add6cc"></a> `00add6cc` | `21 02 80 52` | mov w1,#0x11 | `FALL_THROUGH`
<a id="insn-00add6d0"></a> `00add6d0` | `e5 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add6d4"></a> `00add6d4` | `60 22 00 b9` | str w0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00add6d8"></a> `00add6d8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add6dc"></a> `00add6dc` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00add6e0"></a> `00add6e0` | `e1 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add6e4"></a> `00add6e4` | `60 46 00 b9` | str w0,[x19, #0x44] | `FALL_THROUGH`
<a id="insn-00add6e8"></a> `00add6e8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00add6ec"></a> `00add6ec` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00add6f0"></a> `00add6f0` | `dd 1c e6 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-00add6f4"></a> `00add6f4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00add6f8"></a> `00add6f8` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00add6fc"></a> `00add6fc` | `68 22 01 39` | strb w8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00add700"></a> `00add700` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00add704"></a> `00add704` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00add708"></a> `00add708` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00add5ac`](#insn-00add5ac) 範囲 `[['00add5ac', '00add5fb']]`
  - `FALL_THROUGH` [`00add5f8`](#insn-00add5f8) → [`00add5fc`](#insn-00add5fc)
- ブロック [`00add5fc`](#insn-00add5fc) 範囲 `[['00add5fc', '00add70b']]`

## 命令位置別の参照

- [`00add5ac`](#insn-00add5ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add5b0`](#insn-00add5b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add5c8`](#insn-00add5c8) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add5d8`](#insn-00add5d8) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add5f0`](#insn-00add5f0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add600`](#insn-00add600) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add610`](#insn-00add610) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add620`](#insn-00add620) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add630`](#insn-00add630) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add640`](#insn-00add640) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add650`](#insn-00add650) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add660`](#insn-00add660) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add670`](#insn-00add670) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add680`](#insn-00add680) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add690`](#insn-00add690) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add6a0`](#insn-00add6a0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add6b0`](#insn-00add6b0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add6c0`](#insn-00add6c0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add6d0`](#insn-00add6d0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add6e0`](#insn-00add6e0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add6f0`](#insn-00add6f0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`00add700`](#insn-00add700) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add704`](#insn-00add704) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00add5ac`](#insn-00add5ac)

~~~json
{
  "source": "00add5ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add5b0`](#insn-00add5b0)

~~~json
{
  "source": "00add5b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add5c8`](#insn-00add5c8)

~~~json
{
  "source": "00add5c8",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add5d8`](#insn-00add5d8)

~~~json
{
  "source": "00add5d8",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add5f0`](#insn-00add5f0)

~~~json
{
  "source": "00add5f0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add600`](#insn-00add600)

~~~json
{
  "source": "00add600",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add610`](#insn-00add610)

~~~json
{
  "source": "00add610",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add620`](#insn-00add620)

~~~json
{
  "source": "00add620",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add630`](#insn-00add630)

~~~json
{
  "source": "00add630",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add640`](#insn-00add640)

~~~json
{
  "source": "00add640",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add650`](#insn-00add650)

~~~json
{
  "source": "00add650",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add660`](#insn-00add660)

~~~json
{
  "source": "00add660",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add670`](#insn-00add670)

~~~json
{
  "source": "00add670",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add680`](#insn-00add680)

~~~json
{
  "source": "00add680",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add690`](#insn-00add690)

~~~json
{
  "source": "00add690",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add6a0`](#insn-00add6a0)

~~~json
{
  "source": "00add6a0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add6b0`](#insn-00add6b0)

~~~json
{
  "source": "00add6b0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add6c0`](#insn-00add6c0)

~~~json
{
  "source": "00add6c0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add6d0`](#insn-00add6d0)

~~~json
{
  "source": "00add6d0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add6e0`](#insn-00add6e0)

~~~json
{
  "source": "00add6e0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add6f0`](#insn-00add6f0)

~~~json
{
  "source": "00add6f0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add700`](#insn-00add700)

~~~json
{
  "source": "00add700",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add704`](#insn-00add704)

~~~json
{
  "source": "00add704",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
