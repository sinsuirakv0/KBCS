# 00ae0cac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae0c68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-c3197af0c4e479a83a7041043928d007)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b40684`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-a778c078ad8886dbcf6a368b80c8b370)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0cac",
  "name": "_ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "692ed032d2374547aaea0609d88e7ab30a5c1423b96a336fad3a6c280c87d137",
  "source_text_sha256": "692ed032d2374547aaea0609d88e7ab30a5c1423b96a336fad3a6c280c87d137",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0cac",
        "00ae0ceb"
      ]
    ],
    "bytes_sha256": "de5d7405c952bd93698603cb4a4fe988479e25862a6c23fb3b98527c940a2523",
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

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 449 bytes

~~~c

long _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0118 == 0) {
    DAT_010a0118 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0118;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0cac"></a> `00ae0cac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae0cb0"></a> `00ae0cb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0cb4"></a> `00ae0cb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae0cb8"></a> `00ae0cb8` | `13 2e 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0cbc"></a> `00ae0cbc` | `68 8e 40 f9` | ldr x8,[x19, #0x118] | `FALL_THROUGH`
<a id="insn-00ae0cc0"></a> `00ae0cc0` | `e8 00 00 b5` | cbnz x8,0x00ae0cdc | `CONDITIONAL_JUMP`
<a id="insn-00ae0cc4"></a> `00ae0cc4` | `a3 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00ae0cc8"></a> `00ae0cc8` | `63 64 03 91` | add x3,x3,#0xd9 | `FALL_THROUGH`
<a id="insn-00ae0ccc"></a> `00ae0ccc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae0cd0"></a> `00ae0cd0` | `f0 f4 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0cd4"></a> `00ae0cd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae0cd8"></a> `00ae0cd8` | `60 8e 00 f9` | str x0,[x19, #0x118] | `FALL_THROUGH`
<a id="insn-00ae0cdc"></a> `00ae0cdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0ce0"></a> `00ae0ce0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae0ce4"></a> `00ae0ce4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae0ce8"></a> `00ae0ce8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0cac`](#insn-00ae0cac) 範囲 `[['00ae0cac', '00ae0cc3']]`
  - `CONDITIONAL_JUMP` [`00ae0cc0`](#insn-00ae0cc0) → [`00ae0cdc`](#insn-00ae0cdc)
  - `FALL_THROUGH` [`00ae0cc0`](#insn-00ae0cc0) → [`00ae0cc4`](#insn-00ae0cc4)
- ブロック [`00ae0cc4`](#insn-00ae0cc4) 範囲 `[['00ae0cc4', '00ae0cdb']]`
  - `FALL_THROUGH` [`00ae0cd8`](#insn-00ae0cd8) → [`00ae0cdc`](#insn-00ae0cdc)
- ブロック [`00ae0cdc`](#insn-00ae0cdc) 範囲 `[['00ae0cdc', '00ae0ceb']]`

## 命令位置別の参照

- [`00ae0cac`](#insn-00ae0cac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0cb0`](#insn-00ae0cb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0cbc`](#insn-00ae0cbc) → `010a0118`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0cc0`](#insn-00ae0cc0) → [`00ae0cdc`](#insn-00ae0cdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0cc8`](#insn-00ae0cc8) → `002940d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0cd0`](#insn-00ae0cd0) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae0cd8`](#insn-00ae0cd8) → `010a0118`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0cdc`](#insn-00ae0cdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0cac`](#insn-00ae0cac)

~~~json
{
  "source": "00ae0cac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0cb0`](#insn-00ae0cb0)

~~~json
{
  "source": "00ae0cb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0cbc`](#insn-00ae0cbc)

~~~json
{
  "source": "00ae0cbc",
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0cc0`](#insn-00ae0cc0)

~~~json
{
  "source": "00ae0cc0",
  "target": "00ae0cdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0cc8`](#insn-00ae0cc8)

~~~json
{
  "source": "00ae0cc8",
  "target": "002940d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002940d5",
  "offset": 4,
  "size": 66,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f616e616c79746963",
  "capture_start": "002940d5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae0cd0`](#insn-00ae0cd0)

~~~json
{
  "source": "00ae0cd0",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0cd8`](#insn-00ae0cd8)

~~~json
{
  "source": "00ae0cd8",
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0cdc`](#insn-00ae0cdc)

~~~json
{
  "source": "00ae0cdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
