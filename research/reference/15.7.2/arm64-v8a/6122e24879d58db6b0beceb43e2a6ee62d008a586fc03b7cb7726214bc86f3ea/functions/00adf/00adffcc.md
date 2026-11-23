# 00adffcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae0094`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0094.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-5d8c0922f461e08c078a08ddf68d56f6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adffcc",
  "name": "_ZN8firebase9analytics8internal10FutureData6CreateEv",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f385d5590ca7ae3624e2de878dd834457927e0f9034fb6a83cedf70062e0faa1",
  "source_text_sha256": "f385d5590ca7ae3624e2de878dd834457927e0f9034fb6a83cedf70062e0faa1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adffcc",
        "00ae0007"
      ]
    ],
    "bytes_sha256": "0155f5921a485261db213ded06b93ad6d47d2bc991558567eb5cff854775e886",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddd60](../00bdd/00bddd60.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bddce0](../00bdd/00bddce0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 297 bytes

~~~c

undefined8 _ZN8firebase9analytics8internal10FutureData6CreateEv(void)

{
  undefined8 uVar1;
  
  uVar1 = _Znwm(0x130);
  _ZN8firebase26ReferenceCountedFutureImplC2Em(uVar1,2);
  *(undefined8 *)PTR__ZN8firebase9analytics8internal10FutureData14s_future_data_E_00c1b7a0 = uVar1;
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adffcc"></a> `00adffcc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00adffd0"></a> `00adffd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adffd4"></a> `00adffd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00adffd8"></a> `00adffd8` | `00 26 80 52` | mov w0,#0x130 | `FALL_THROUGH`
<a id="insn-00adffdc"></a> `00adffdc` | `d9 eb 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00adffe0"></a> `00adffe0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adffe4"></a> `00adffe4` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00adffe8"></a> `00adffe8` | `3e f7 03 94` | bl 0x00bddce0 | `UNCONDITIONAL_CALL`
<a id="insn-00adffec"></a> `00adffec` | `e8 09 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00adfff0"></a> `00adfff0` | `08 d1 43 f9` | ldr x8,[x8, #0x7a0] | `FALL_THROUGH`
<a id="insn-00adfff4"></a> `00adfff4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfff8"></a> `00adfff8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfffc"></a> `00adfffc` | `13 01 00 f9` | str x19,[x8] | `FALL_THROUGH`
<a id="insn-00ae0000"></a> `00ae0000` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae0004"></a> `00ae0004` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adffcc`](#insn-00adffcc) 範囲 `[['00adffcc', '00ae0007']]`

## 命令位置別の参照

- [`00adffcc`](#insn-00adffcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adffd0`](#insn-00adffd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adffdc`](#insn-00adffdc) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00adffe8`](#insn-00adffe8) → [`00bddce0`](../00bdd/00bddce0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddce0` · 推定シンボル `None` · 推定型 `None`
- [`00adfff0`](#insn-00adfff0) → `00c1b7a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adfff4`](#insn-00adfff4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfffc`](#insn-00adfffc) → `0109ff68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase9analytics8internal10FutureData14s_future_data_E` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adffcc`](#insn-00adffcc)

~~~json
{
  "source": "00adffcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adffd0`](#insn-00adffd0)

~~~json
{
  "source": "00adffd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adffdc`](#insn-00adffdc)

~~~json
{
  "source": "00adffdc",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adffe8`](#insn-00adffe8)

~~~json
{
  "source": "00adffe8",
  "target": "00bddce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfff0`](#insn-00adfff0)

~~~json
{
  "source": "00adfff0",
  "target": "00c1b7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b7a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfff4`](#insn-00adfff4)

~~~json
{
  "source": "00adfff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfffc`](#insn-00adfffc)

~~~json
{
  "source": "00adfffc",
  "target": "0109ff68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
