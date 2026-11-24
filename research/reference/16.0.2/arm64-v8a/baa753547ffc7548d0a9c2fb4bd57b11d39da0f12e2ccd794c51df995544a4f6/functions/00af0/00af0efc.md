# 00af0efc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af0e60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0e60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-f3876441961350adcf419e410713cb82)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0043.md#review-5884ed91475042a1a9a740975eb4615a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af0efc",
  "name": "FUN_00af0efc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2485bf30a29fc0a78ee701d76d8cc567e8e181bf88db7ba7931bb21a42527604",
  "source_text_sha256": "2485bf30a29fc0a78ee701d76d8cc567e8e181bf88db7ba7931bb21a42527604",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af0efc",
        "00af0f2f"
      ]
    ],
    "bytes_sha256": "965477a12bd5676f659049661554b4ea10f50a7c7275137b18d6c25f966366d3",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 321 bytes

~~~c

void FUN_00af0efc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00af0f04 to 00bf0f47 has its CatchHandler @ 00af1050 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8e7c8;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af0efc"></a> `00af0efc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af0f00"></a> `00af0f00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0f04"></a> `00af0f04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af0f08"></a> `00af0f08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af0f0c"></a> `00af0f0c` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00af0f10"></a> `00af0f10` | `14 9c 05 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f14"></a> `00af0f14` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af0f18"></a> `00af0f18` | `e8 0c 00 d0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00af0f1c"></a> `00af0f1c` | `08 21 1f 91` | add x8,x8,#0x7c8 | `FALL_THROUGH`
<a id="insn-00af0f20"></a> `00af0f20` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00af0f24"></a> `00af0f24` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0f28"></a> `00af0f28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af0f2c"></a> `00af0f2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af0efc`](#insn-00af0efc) 範囲 `[['00af0efc', '00af0f03']]`
  - `FALL_THROUGH` [`00af0f00`](#insn-00af0f00) → [`00af0f04`](#insn-00af0f04)
- ブロック [`00af0f04`](#insn-00af0f04) 範囲 `[['00af0f04', '00af0f2f']]`

## 命令位置別の参照

- [`00af0efc`](#insn-00af0efc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f00`](#insn-00af0f00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f10`](#insn-00af0f10) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00af0f20`](#insn-00af0f20) → `00c8e7c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00af0f24`](#insn-00af0f24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f28`](#insn-00af0f28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af0efc`](#insn-00af0efc)

~~~json
{
  "source": "00af0efc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f00`](#insn-00af0f00)

~~~json
{
  "source": "00af0f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f10`](#insn-00af0f10)

~~~json
{
  "source": "00af0f10",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f20`](#insn-00af0f20)

~~~json
{
  "source": "00af0f20",
  "target": "00c8e7c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e7c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00af0f24`](#insn-00af0f24)

~~~json
{
  "source": "00af0f24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f28`](#insn-00af0f28)

~~~json
{
  "source": "00af0f28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
