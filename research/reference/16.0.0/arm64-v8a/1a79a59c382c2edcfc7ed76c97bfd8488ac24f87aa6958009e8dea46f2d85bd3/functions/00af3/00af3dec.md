# 00af3dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0015.md#review-4900c090337bc2696116a75c1c36b6b8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af4214`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4214.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-d646ae47f7a37025c6e7fd7a33fa20d2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af3dec",
  "name": "FUN_00af3dec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "189650ce466002a521ca39087c4dac6ba3e2d4f348540d0281673a9c2c78e0ed",
  "source_text_sha256": "189650ce466002a521ca39087c4dac6ba3e2d4f348540d0281673a9c2c78e0ed",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af3dec",
        "00af3e2b"
      ]
    ],
    "bytes_sha256": "92cb497d828a939d41863ef169b233f42dee86cb6d45ecc4364fad700c846363",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f7900](../005f7/005f7900.md)
- [005f87e0](../005f8/005f87e0.md)
- [005f8e40](../005f8/005f8e40.md)
- [005f9670](../005f9/005f9670.md)
- [005fb400](../005fb/005fb400.md)
- [005fdc18](../005fd/005fdc18.md)
- [00700ab8](../00700/00700ab8.md)
- [00713318](../00713/00713318.md)
- [0071421c](../00714/0071421c.md)
- [00714f4c](../00714/00714f4c.md)
- [007154c0](../00715/007154c0.md)
- [00716b40](../00716/00716b40.md)
- [00716d50](../00716/00716d50.md)
- [00a51dcc](../00a51/00a51dcc.md)
- [00af2460](../00af2/00af2460.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af3dec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848d4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af3dec"></a> `00af3dec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af3df0"></a> `00af3df0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3df4"></a> `00af3df4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af3df8"></a> `00af3df8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af3dfc"></a> `00af3dfc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af3e00"></a> `00af3e00` | `ae 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3e04"></a> `00af3e04` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af3e08"></a> `00af3e08` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af3e0c"></a> `00af3e0c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af3e10"></a> `00af3e10` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af3e14"></a> `00af3e14` | `89 1a 89 52` | mov w9,#0x48d4 | `FALL_THROUGH`
<a id="insn-00af3e18"></a> `00af3e18` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af3e1c"></a> `00af3e1c` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af3e20"></a> `00af3e20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3e24"></a> `00af3e24` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af3e28"></a> `00af3e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af3dec`](#insn-00af3dec) 範囲 `[['00af3dec', '00af3e2b']]`

## 命令位置別の参照

- [`00af3dec`](#insn-00af3dec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3df0`](#insn-00af3df0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e00`](#insn-00af3e00) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af3e20`](#insn-00af3e20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e24`](#insn-00af3e24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af3dec`](#insn-00af3dec)

~~~json
{
  "source": "00af3dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3df0`](#insn-00af3df0)

~~~json
{
  "source": "00af3df0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e00`](#insn-00af3e00)

~~~json
{
  "source": "00af3e00",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3e20`](#insn-00af3e20)

~~~json
{
  "source": "00af3e20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e24`](#insn-00af3e24)

~~~json
{
  "source": "00af3e24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
