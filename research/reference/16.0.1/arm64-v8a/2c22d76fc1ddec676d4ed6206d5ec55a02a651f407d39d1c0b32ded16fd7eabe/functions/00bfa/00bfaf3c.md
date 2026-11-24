# 00bfaf3c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfab14`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-ca6c78eba0500e624be36afede0bd23a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfafd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfafd8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0011.md#compare-dc391372d390537c1ceb297eb0003719)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaf3c",
  "name": "_ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cdb0063d584407980d4ba2f0c75c677f0cd7ed0a068256f21f7143d4c0712ad",
  "source_text_sha256": "2cdb0063d584407980d4ba2f0c75c677f0cd7ed0a068256f21f7143d4c0712ad",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaf3c",
        "00bfaf7b"
      ]
    ],
    "bytes_sha256": "a908a323fbf764b9bc0b3739e01054951f48eaf2af604d60dd139557f3f16069",
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

- [00c5e150](../00c5e/00c5e150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 437 bytes

~~~c

void _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
               (long *param_1,undefined8 param_2,undefined8 *param_3)

{
  _ZNSt6__ndk112system_errorC2ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
            (param_1,*param_3,param_3[1],param_2);
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_base7failureE_00c9bae8 + 0x10);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaf3c"></a> `00bfaf3c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaf40"></a> `00bfaf40` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfaf44"></a> `00bfaf44` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaf48"></a> `00bfaf48` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaf4c"></a> `00bfaf4c` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bfaf50"></a> `00bfaf50` | `41 08 40 a9` | ldp x1,x2,[x2] | `FALL_THROUGH`
<a id="insn-00bfaf54"></a> `00bfaf54` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfaf58"></a> `00bfaf58` | `7e 8c 01 94` | bl 0x00c5e150 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaf5c"></a> `00bfaf5c` | `08 05 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfaf60"></a> `00bfaf60` | `08 75 45 f9` | ldr x8,[x8, #0xae8] | `FALL_THROUGH`
<a id="insn-00bfaf64"></a> `00bfaf64` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bfaf68"></a> `00bfaf68` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfaf6c"></a> `00bfaf6c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaf70"></a> `00bfaf70` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfaf74"></a> `00bfaf74` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaf78"></a> `00bfaf78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaf3c`](#insn-00bfaf3c) 範囲 `[['00bfaf3c', '00bfaf7b']]`

## 命令位置別の参照

- [`00bfaf40`](#insn-00bfaf40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf44`](#insn-00bfaf44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf58`](#insn-00bfaf58) → [`00c5e150`](../00c5e/00c5e150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e150` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf60`](#insn-00bfaf60) → `00c9bae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfaf68`](#insn-00bfaf68) → `00c92d80`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bfaf6c`](#insn-00bfaf6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf70`](#insn-00bfaf70) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaf40`](#insn-00bfaf40)

~~~json
{
  "source": "00bfaf40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf44`](#insn-00bfaf44)

~~~json
{
  "source": "00bfaf44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf58`](#insn-00bfaf58)

~~~json
{
  "source": "00bfaf58",
  "target": "00c5e150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaf60`](#insn-00bfaf60)

~~~json
{
  "source": "00bfaf60",
  "target": "00c9bae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bae8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfaf68`](#insn-00bfaf68)

~~~json
{
  "source": "00bfaf68",
  "target": "00c92d80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92d70",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bfaf6c`](#insn-00bfaf6c)

~~~json
{
  "source": "00bfaf6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf70`](#insn-00bfaf70)

~~~json
{
  "source": "00bfaf70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
