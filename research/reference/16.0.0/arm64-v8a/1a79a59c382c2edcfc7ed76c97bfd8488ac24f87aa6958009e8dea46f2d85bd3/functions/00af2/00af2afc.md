# 00af2afc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0165.md#review-1367369269bd00bb31d1da859d203778)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af2f24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af2f24.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-32c7c9e0f2af744c895353dee6903244)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af2afc",
  "name": "FUN_00af2afc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a19b4035134673fd463f9a4702d2307ff47fafee909bb9c2add169e0f1629bcb",
  "source_text_sha256": "a19b4035134673fd463f9a4702d2307ff47fafee909bb9c2add169e0f1629bcb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af2afc",
        "00af2b2f"
      ]
    ],
    "bytes_sha256": "ab51848671a33a39fd262712b6a98f734e6d537101d448d6aaa892fb446bbeaf",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fdc18](../005fd/005fdc18.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

undefined4 FUN_00af2afc(int param_1)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x84920);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af2afc"></a> `00af2afc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af2b00"></a> `00af2b00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af2b04"></a> `00af2b04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af2b08"></a> `00af2b08` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00af2b0c"></a> `00af2b0c` | `6b 7a f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af2b10"></a> `00af2b10` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af2b14"></a> `00af2b14` | `09 24 89 52` | mov w9,#0x4920 | `FALL_THROUGH`
<a id="insn-00af2b18"></a> `00af2b18` | `68 02 28 9b` | smaddl x8,w19,w8,x0 | `FALL_THROUGH`
<a id="insn-00af2b1c"></a> `00af2b1c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af2b20"></a> `00af2b20` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af2b24"></a> `00af2b24` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af2b28"></a> `00af2b28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af2b2c"></a> `00af2b2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af2afc`](#insn-00af2afc) 範囲 `[['00af2afc', '00af2b2f']]`

## 命令位置別の参照

- [`00af2afc`](#insn-00af2afc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2b00`](#insn-00af2b00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2b0c`](#insn-00af2b0c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af2b24`](#insn-00af2b24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2b28`](#insn-00af2b28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af2afc`](#insn-00af2afc)

~~~json
{
  "source": "00af2afc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2b00`](#insn-00af2b00)

~~~json
{
  "source": "00af2b00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2b0c`](#insn-00af2b0c)

~~~json
{
  "source": "00af2b0c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af2b24`](#insn-00af2b24)

~~~json
{
  "source": "00af2b24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2b28`](#insn-00af2b28)

~~~json
{
  "source": "00af2b28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
