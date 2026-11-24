# 009ddecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009dcf20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcf20.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0025.md#compare-c5534c53710c60768139e8f170fb64bc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009ddecc",
  "name": "FUN_009ddecc",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09b0168f8df72c77ddbe4933917289a30937a23d1bca523b6dace51e58ac7ff6",
  "source_text_sha256": "09b0168f8df72c77ddbe4933917289a30937a23d1bca523b6dace51e58ac7ff6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009ddecc",
        "009ddf97"
      ]
    ],
    "bytes_sha256": "f8e84618dbc90366352f47ba5b8878143f4458781152758f5fd3211f591ce4f2",
    "instruction_count": 51,
    "instruction_bytes": 204,
    "body_bytes": 204,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0063b0a4](../0063b/0063b0a4.md)
- [0063b93c](../0063b/0063b93c.md)
- [0063c088](../0063c/0063c088.md)
- [0064f0a8](../0064f/0064f0a8.md)
- [006c1340](../006c1/006c1340.md)
- [006c15a4](../006c1/006c15a4.md)
- [006c2420](../006c2/006c2420.md)
- [006d4244](../006d4/006d4244.md)
- [006dd66c](../006dd/006dd66c.md)
- [006deb90](../006de/006deb90.md)
- [006dee9c](../006de/006dee9c.md)
- [006e22b0](../006e2/006e22b0.md)
- [006e3728](../006e3/006e3728.md)
- [006f28dc](../006f2/006f28dc.md)
- [0076a1b8](../0076a/0076a1b8.md)
- [008dd120](../008dd/008dd120.md)
- [008e76ac](../008e7/008e76ac.md)
- [008f09f4](../008f0/008f09f4.md)
- [008f4044](../008f4/008f4044.md)
- [0098ec08](../0098e/0098ec08.md)
- [00a76e10](../00a76/00a76e10.md)

## 呼び出し先

- [0085c2a8](../0085c/0085c2a8.md)
- [0085c2b0](../0085c/0085c2b0.md)
- [0085c2b8](../0085c/0085c2b8.md)
- [0085c2c0](../0085c/0085c2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1529 bytes

~~~c

undefined8 FUN_009ddecc(undefined8 param_1,int param_2,int param_3,int param_4,int param_5)

{
  int iVar1;
  
                    /* try { // try from 009ddee8 to 00addeef has its CatchHandler @ 009ddfd4 */
  iVar1 = FUN_0085c2a8();
  if (param_2 <= iVar1) {
                    /* try { // try from 009ddf04 to 00addf23 has its CatchHandler @ 009ddfec */
    iVar1 = FUN_0085c2a8(param_1);
    if ((iVar1 <= param_4 + param_2) && (iVar1 = FUN_0085c2b0(param_1), param_3 <= iVar1)) {
      iVar1 = FUN_0085c2b0(param_1);
                    /* try { // try from 009ddf38 to 00addf3f has its CatchHandler @ 009ddfb0 */
                    /* try { // try from 009ddf54 to 00addf5b has its CatchHandler @ 009ddf60 */
                    /* catch() { ... } // from try @ 009ddc3c with catch @ 009ddf5c
                       try { // try from 009ddf5c to 00ade02f has its CatchHandler @ 009dd934 */
                    /* catch() { ... } // from try @ 009ddc08 with catch @ 009ddf60
                       catch() { ... } // from try @ 009ddf54 with catch @ 009ddf60 */
      if (((iVar1 <= param_5 + param_3) &&
          (((iVar1 = FUN_0085c2b8(param_1), param_2 <= iVar1 &&
            (iVar1 = FUN_0085c2b8(param_1), iVar1 <= param_4 + param_2)) &&
           (iVar1 = FUN_0085c2c0(param_1), param_3 <= iVar1)))) &&
         (iVar1 = FUN_0085c2c0(param_1), iVar1 <= param_5 + param_3)) {
        return 1;
      }
    }
  }
                    /* catch() { ... } // from try @ 009dde44 with catch @ 009ddf78 */
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009ddecc"></a> `009ddecc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-009dded0"></a> `009dded0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dded4"></a> `009dded4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dded8"></a> `009dded8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ddedc"></a> `009ddedc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009ddee0"></a> `009ddee0` | `f6 03 04 2a` | mov w22,w4 | `FALL_THROUGH`
<a id="insn-009ddee4"></a> `009ddee4` | `f7 03 03 2a` | mov w23,w3 | `FALL_THROUGH`
<a id="insn-009ddee8"></a> `009ddee8` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-009ddeec"></a> `009ddeec` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-009ddef0"></a> `009ddef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009ddef4"></a> `009ddef4` | `ed f8 f9 97` | bl 0x0085c2a8 | `UNCONDITIONAL_CALL`
<a id="insn-009ddef8"></a> `009ddef8` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-009ddefc"></a> `009ddefc` | `eb 03 00 54` | b.lt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf00"></a> `009ddf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf04"></a> `009ddf04` | `f7 02 15 0b` | add w23,w23,w21 | `FALL_THROUGH`
<a id="insn-009ddf08"></a> `009ddf08` | `e8 f8 f9 97` | bl 0x0085c2a8 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf0c"></a> `009ddf0c` | `1f 00 17 6b` | cmp w0,w23 | `FALL_THROUGH`
<a id="insn-009ddf10"></a> `009ddf10` | `4c 03 00 54` | b.gt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf14"></a> `009ddf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf18"></a> `009ddf18` | `e6 f8 f9 97` | bl 0x0085c2b0 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf1c"></a> `009ddf1c` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-009ddf20"></a> `009ddf20` | `cb 02 00 54` | b.lt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf24"></a> `009ddf24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf28"></a> `009ddf28` | `d6 02 14 0b` | add w22,w22,w20 | `FALL_THROUGH`
<a id="insn-009ddf2c"></a> `009ddf2c` | `e1 f8 f9 97` | bl 0x0085c2b0 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf30"></a> `009ddf30` | `1f 00 16 6b` | cmp w0,w22 | `FALL_THROUGH`
<a id="insn-009ddf34"></a> `009ddf34` | `2c 02 00 54` | b.gt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf38"></a> `009ddf38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf3c"></a> `009ddf3c` | `df f8 f9 97` | bl 0x0085c2b8 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf40"></a> `009ddf40` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-009ddf44"></a> `009ddf44` | `ab 01 00 54` | b.lt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf48"></a> `009ddf48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf4c"></a> `009ddf4c` | `db f8 f9 97` | bl 0x0085c2b8 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf50"></a> `009ddf50` | `1f 00 17 6b` | cmp w0,w23 | `FALL_THROUGH`
<a id="insn-009ddf54"></a> `009ddf54` | `2c 01 00 54` | b.gt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf58"></a> `009ddf58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf5c"></a> `009ddf5c` | `d9 f8 f9 97` | bl 0x0085c2c0 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf60"></a> `009ddf60` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-009ddf64"></a> `009ddf64` | `ab 00 00 54` | b.lt 0x009ddf78 | `CONDITIONAL_JUMP`
<a id="insn-009ddf68"></a> `009ddf68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ddf6c"></a> `009ddf6c` | `d5 f8 f9 97` | bl 0x0085c2c0 | `UNCONDITIONAL_CALL`
<a id="insn-009ddf70"></a> `009ddf70` | `1f 00 16 6b` | cmp w0,w22 | `FALL_THROUGH`
<a id="insn-009ddf74"></a> `009ddf74` | `ed 00 00 54` | b.le 0x009ddf90 | `CONDITIONAL_JUMP`
<a id="insn-009ddf78"></a> `009ddf78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009ddf7c"></a> `009ddf7c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ddf80"></a> `009ddf80` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ddf84"></a> `009ddf84` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ddf88"></a> `009ddf88` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-009ddf8c"></a> `009ddf8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009ddf90"></a> `009ddf90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ddf94"></a> `009ddf94` | `fa ff ff 17` | b 0x009ddf7c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`009ddecc`](#insn-009ddecc) 範囲 `[['009ddecc', '009ddee7']]`
  - `FALL_THROUGH` [`009ddee4`](#insn-009ddee4) → [`009ddee8`](#insn-009ddee8)
- ブロック [`009ddee8`](#insn-009ddee8) 範囲 `[['009ddee8', '009ddeff']]`
  - `CONDITIONAL_JUMP` [`009ddefc`](#insn-009ddefc) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddefc`](#insn-009ddefc) → [`009ddf00`](#insn-009ddf00)
- ブロック [`009ddf00`](#insn-009ddf00) 範囲 `[['009ddf00', '009ddf03']]`
  - `FALL_THROUGH` [`009ddf00`](#insn-009ddf00) → [`009ddf04`](#insn-009ddf04)
- ブロック [`009ddf04`](#insn-009ddf04) 範囲 `[['009ddf04', '009ddf13']]`
  - `CONDITIONAL_JUMP` [`009ddf10`](#insn-009ddf10) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddf10`](#insn-009ddf10) → [`009ddf14`](#insn-009ddf14)
- ブロック [`009ddf14`](#insn-009ddf14) 範囲 `[['009ddf14', '009ddf23']]`
  - `CONDITIONAL_JUMP` [`009ddf20`](#insn-009ddf20) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddf20`](#insn-009ddf20) → [`009ddf24`](#insn-009ddf24)
- ブロック [`009ddf24`](#insn-009ddf24) 範囲 `[['009ddf24', '009ddf37']]`
  - `CONDITIONAL_JUMP` [`009ddf34`](#insn-009ddf34) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddf34`](#insn-009ddf34) → [`009ddf38`](#insn-009ddf38)
- ブロック [`009ddf38`](#insn-009ddf38) 範囲 `[['009ddf38', '009ddf47']]`
  - `CONDITIONAL_JUMP` [`009ddf44`](#insn-009ddf44) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddf44`](#insn-009ddf44) → [`009ddf48`](#insn-009ddf48)
- ブロック [`009ddf48`](#insn-009ddf48) 範囲 `[['009ddf48', '009ddf53']]`
  - `FALL_THROUGH` [`009ddf50`](#insn-009ddf50) → [`009ddf54`](#insn-009ddf54)
- ブロック [`009ddf54`](#insn-009ddf54) 範囲 `[['009ddf54', '009ddf57']]`
  - `CONDITIONAL_JUMP` [`009ddf54`](#insn-009ddf54) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddf54`](#insn-009ddf54) → [`009ddf58`](#insn-009ddf58)
- ブロック [`009ddf58`](#insn-009ddf58) 範囲 `[['009ddf58', '009ddf5b']]`
  - `FALL_THROUGH` [`009ddf58`](#insn-009ddf58) → [`009ddf5c`](#insn-009ddf5c)
- ブロック [`009ddf5c`](#insn-009ddf5c) 範囲 `[['009ddf5c', '009ddf5f']]`
  - `FALL_THROUGH` [`009ddf5c`](#insn-009ddf5c) → [`009ddf60`](#insn-009ddf60)
- ブロック [`009ddf60`](#insn-009ddf60) 範囲 `[['009ddf60', '009ddf67']]`
  - `CONDITIONAL_JUMP` [`009ddf64`](#insn-009ddf64) → [`009ddf78`](#insn-009ddf78)
  - `FALL_THROUGH` [`009ddf64`](#insn-009ddf64) → [`009ddf68`](#insn-009ddf68)
- ブロック [`009ddf68`](#insn-009ddf68) 範囲 `[['009ddf68', '009ddf77']]`
  - `CONDITIONAL_JUMP` [`009ddf74`](#insn-009ddf74) → [`009ddf90`](#insn-009ddf90)
  - `FALL_THROUGH` [`009ddf74`](#insn-009ddf74) → [`009ddf78`](#insn-009ddf78)
- ブロック [`009ddf78`](#insn-009ddf78) 範囲 `[['009ddf78', '009ddf7b']]`
  - `FALL_THROUGH` [`009ddf78`](#insn-009ddf78) → [`009ddf7c`](#insn-009ddf7c)
- ブロック [`009ddf7c`](#insn-009ddf7c) 範囲 `[['009ddf7c', '009ddf8f']]`
- ブロック [`009ddf90`](#insn-009ddf90) 範囲 `[['009ddf90', '009ddf97']]`
  - `UNCONDITIONAL_JUMP` [`009ddf94`](#insn-009ddf94) → [`009ddf7c`](#insn-009ddf7c)

## 命令位置別の参照

- [`009ddecc`](#insn-009ddecc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dded0`](#insn-009dded0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dded4`](#insn-009dded4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dded8`](#insn-009dded8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddef4`](#insn-009ddef4) → [`0085c2a8`](../0085c/0085c2a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2a8` · 推定シンボル `None` · 推定型 `None`
- [`009ddefc`](#insn-009ddefc) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf08`](#insn-009ddf08) → [`0085c2a8`](../0085c/0085c2a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2a8` · 推定シンボル `None` · 推定型 `None`
- [`009ddf10`](#insn-009ddf10) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf18`](#insn-009ddf18) → [`0085c2b0`](../0085c/0085c2b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2b0` · 推定シンボル `None` · 推定型 `None`
- [`009ddf20`](#insn-009ddf20) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf2c`](#insn-009ddf2c) → [`0085c2b0`](../0085c/0085c2b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2b0` · 推定シンボル `None` · 推定型 `None`
- [`009ddf34`](#insn-009ddf34) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf3c`](#insn-009ddf3c) → [`0085c2b8`](../0085c/0085c2b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2b8` · 推定シンボル `None` · 推定型 `None`
- [`009ddf44`](#insn-009ddf44) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf4c`](#insn-009ddf4c) → [`0085c2b8`](../0085c/0085c2b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2b8` · 推定シンボル `None` · 推定型 `None`
- [`009ddf54`](#insn-009ddf54) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf5c`](#insn-009ddf5c) → [`0085c2c0`](../0085c/0085c2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2c0` · 推定シンボル `None` · 推定型 `None`
- [`009ddf64`](#insn-009ddf64) → [`009ddf78`](#insn-009ddf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf6c`](#insn-009ddf6c) → [`0085c2c0`](../0085c/0085c2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c2c0` · 推定シンボル `None` · 推定型 `None`
- [`009ddf74`](#insn-009ddf74) → [`009ddf90`](#insn-009ddf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf7c`](#insn-009ddf7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf80`](#insn-009ddf80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf84`](#insn-009ddf84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf88`](#insn-009ddf88) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ddf94`](#insn-009ddf94) → [`009ddf7c`](#insn-009ddf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009ddecc`](#insn-009ddecc)

~~~json
{
  "source": "009ddecc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dded0`](#insn-009dded0)

~~~json
{
  "source": "009dded0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dded4`](#insn-009dded4)

~~~json
{
  "source": "009dded4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dded8`](#insn-009dded8)

~~~json
{
  "source": "009dded8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddef4`](#insn-009ddef4)

~~~json
{
  "source": "009ddef4",
  "target": "0085c2a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddefc`](#insn-009ddefc)

~~~json
{
  "source": "009ddefc",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf08`](#insn-009ddf08)

~~~json
{
  "source": "009ddf08",
  "target": "0085c2a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf10`](#insn-009ddf10)

~~~json
{
  "source": "009ddf10",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf18`](#insn-009ddf18)

~~~json
{
  "source": "009ddf18",
  "target": "0085c2b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf20`](#insn-009ddf20)

~~~json
{
  "source": "009ddf20",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf2c`](#insn-009ddf2c)

~~~json
{
  "source": "009ddf2c",
  "target": "0085c2b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf34`](#insn-009ddf34)

~~~json
{
  "source": "009ddf34",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf3c`](#insn-009ddf3c)

~~~json
{
  "source": "009ddf3c",
  "target": "0085c2b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf44`](#insn-009ddf44)

~~~json
{
  "source": "009ddf44",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf4c`](#insn-009ddf4c)

~~~json
{
  "source": "009ddf4c",
  "target": "0085c2b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf54`](#insn-009ddf54)

~~~json
{
  "source": "009ddf54",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf5c`](#insn-009ddf5c)

~~~json
{
  "source": "009ddf5c",
  "target": "0085c2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf64`](#insn-009ddf64)

~~~json
{
  "source": "009ddf64",
  "target": "009ddf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf6c`](#insn-009ddf6c)

~~~json
{
  "source": "009ddf6c",
  "target": "0085c2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ddf74`](#insn-009ddf74)

~~~json
{
  "source": "009ddf74",
  "target": "009ddf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf7c`](#insn-009ddf7c)

~~~json
{
  "source": "009ddf7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf80`](#insn-009ddf80)

~~~json
{
  "source": "009ddf80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf84`](#insn-009ddf84)

~~~json
{
  "source": "009ddf84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf88`](#insn-009ddf88)

~~~json
{
  "source": "009ddf88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ddf94`](#insn-009ddf94)

~~~json
{
  "source": "009ddf94",
  "target": "009ddf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
