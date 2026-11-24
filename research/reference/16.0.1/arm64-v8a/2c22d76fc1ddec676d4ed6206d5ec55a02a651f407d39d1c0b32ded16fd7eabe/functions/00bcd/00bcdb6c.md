# 00bcdb6c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd744`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-3e9d4d431fd9a1935ea25b37ac241728)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcdc08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-7dd154849700a2fd29a42737b82c7ec0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdb6c",
  "name": "_ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ace90afe5e708fb2676ca8c06d5311774b28d0adaf89135ed019f791c13a1ff7",
  "source_text_sha256": "ace90afe5e708fb2676ca8c06d5311774b28d0adaf89135ed019f791c13a1ff7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdb6c",
        "00bcdbab"
      ]
    ],
    "bytes_sha256": "bee044fff8b061f7f2fa620a0866ad608a9c6fca6a5d9834a41aebaa550acd8e",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5d9f0](../00c5d/00c5d9f0.md)
- [00c5dc30](../00c5d/00c5dc30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 441 bytes

~~~c

void _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,long param_3)

{
  _ZN8firebase5Mutex7AcquireEv(param_3 + 700);
  *(undefined1 *)(param_3 + 0x2b8) = 0;
  _ZN8firebase5Mutex7ReleaseEv(param_3 + 700);
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdb6c"></a> `00bcdb6c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdb70"></a> `00bcdb70` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdb74"></a> `00bcdb74` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdb78"></a> `00bcdb78` | `54 f0 0a 91` | add x20,x2,#0x2bc | `FALL_THROUGH`
<a id="insn-00bcdb7c"></a> `00bcdb7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb80"></a> `00bcdb80` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bcdb84"></a> `00bcdb84` | `9f 33 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb88"></a> `00bcdb88` | `7f e2 0a 39` | strb wzr,[x19, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bcdb8c"></a> `00bcdb8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb90"></a> `00bcdb90` | `a0 33 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb94"></a> `00bcdb94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdb98"></a> `00bcdb98` | `26 40 02 94` | bl 0x00c5dc30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb9c"></a> `00bcdb9c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdba0"></a> `00bcdba0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdba4"></a> `00bcdba4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdba8"></a> `00bcdba8` | `92 3f 02 14` | b 0x00c5d9f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdb6c`](#insn-00bcdb6c) 範囲 `[['00bcdb6c', '00bcdbab']]`

## 命令位置別の参照

- [`00bcdb6c`](#insn-00bcdb6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb70`](#insn-00bcdb70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb84`](#insn-00bcdb84) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb90`](#insn-00bcdb90) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb98`](#insn-00bcdb98) → [`00c5dc30`](../00c5d/00c5dc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc30` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb9c`](#insn-00bcdb9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdba8`](#insn-00bcdba8) → [`00c5d9f0`](../00c5d/00c5d9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d9f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdb6c`](#insn-00bcdb6c)

~~~json
{
  "source": "00bcdb6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb70`](#insn-00bcdb70)

~~~json
{
  "source": "00bcdb70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb84`](#insn-00bcdb84)

~~~json
{
  "source": "00bcdb84",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb90`](#insn-00bcdb90)

~~~json
{
  "source": "00bcdb90",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb98`](#insn-00bcdb98)

~~~json
{
  "source": "00bcdb98",
  "target": "00c5dc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb9c`](#insn-00bcdb9c)

~~~json
{
  "source": "00bcdb9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdba8`](#insn-00bcdba8)

~~~json
{
  "source": "00bcdba8",
  "target": "00c5d9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
