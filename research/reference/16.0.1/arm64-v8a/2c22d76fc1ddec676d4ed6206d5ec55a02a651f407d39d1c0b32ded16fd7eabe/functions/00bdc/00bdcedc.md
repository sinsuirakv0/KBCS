# 00bdcedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdcab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-685dcfe59129378f2fd3ae8701bad053)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcf78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-fb3cecf59e12d090715e03843e562b37)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcedc",
  "name": "_ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98b0d79bb74ba579bf87ac40a0f2ca63a7ccc9fd7c3234568e5e1ef65f2bc540",
  "source_text_sha256": "98b0d79bb74ba579bf87ac40a0f2ca63a7ccc9fd7c3234568e5e1ef65f2bc540",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcedc",
        "00bdcf1f"
      ]
    ],
    "bytes_sha256": "275130a35377542d05fd45bdc5f1533d83261fba642187ef1d873debdc9eaaa5",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 447 bytes

~~~c

long _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126d00 == 0) {
    DAT_01126d00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  return DAT_01126d00;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcedc"></a> `00bdcedc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcee0"></a> `00bdcee0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcee4"></a> `00bdcee4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcee8"></a> `00bdcee8` | `53 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdceec"></a> `00bdceec` | `68 82 46 f9` | ldr x8,[x19, #0xd00] | `FALL_THROUGH`
<a id="insn-00bdcef0"></a> `00bdcef0` | `08 01 00 b5` | cbnz x8,0x00bdcf10 | `CONDITIONAL_JUMP`
<a id="insn-00bdcef4"></a> `00bdcef4` | `03 b7 ff 90` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdcef8"></a> `00bdcef8` | `63 40 09 91` | add x3,x3,#0x250 | `FALL_THROUGH`
<a id="insn-00bdcefc"></a> `00bdcefc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdcf00"></a> `00bdcf00` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdcf04"></a> `00bdcf04` | `03 f8 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcf08"></a> `00bdcf08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdcf0c"></a> `00bdcf0c` | `60 82 06 f9` | str x0,[x19, #0xd00] | `FALL_THROUGH`
<a id="insn-00bdcf10"></a> `00bdcf10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcf14"></a> `00bdcf14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdcf18"></a> `00bdcf18` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdcf1c"></a> `00bdcf1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcedc`](#insn-00bdcedc) 範囲 `[['00bdcedc', '00bdcef3']]`
  - `CONDITIONAL_JUMP` [`00bdcef0`](#insn-00bdcef0) → [`00bdcf10`](#insn-00bdcf10)
  - `FALL_THROUGH` [`00bdcef0`](#insn-00bdcef0) → [`00bdcef4`](#insn-00bdcef4)
- ブロック [`00bdcef4`](#insn-00bdcef4) 範囲 `[['00bdcef4', '00bdcf0f']]`
  - `FALL_THROUGH` [`00bdcf0c`](#insn-00bdcf0c) → [`00bdcf10`](#insn-00bdcf10)
- ブロック [`00bdcf10`](#insn-00bdcf10) 範囲 `[['00bdcf10', '00bdcf1f']]`

## 命令位置別の参照

- [`00bdcedc`](#insn-00bdcedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcee0`](#insn-00bdcee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdceec`](#insn-00bdceec) → `01126d00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcef0`](#insn-00bdcef0) → [`00bdcf10`](#insn-00bdcf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcef8`](#insn-00bdcef8) → `002bc250`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdcf04`](#insn-00bdcf04) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf0c`](#insn-00bdcf0c) → `01126d00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcf10`](#insn-00bdcf10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcedc`](#insn-00bdcedc)

~~~json
{
  "source": "00bdcedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcee0`](#insn-00bdcee0)

~~~json
{
  "source": "00bdcee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdceec`](#insn-00bdceec)

~~~json
{
  "source": "00bdceec",
  "target": "01126d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcef0`](#insn-00bdcef0)

~~~json
{
  "source": "00bdcef0",
  "target": "00bdcf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcef8`](#insn-00bdcef8)

~~~json
{
  "source": "00bdcef8",
  "target": "002bc250",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc24c",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc24c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdcf04`](#insn-00bdcf04)

~~~json
{
  "source": "00bdcf04",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcf0c`](#insn-00bdcf0c)

~~~json
{
  "source": "00bdcf0c",
  "target": "01126d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcf10`](#insn-00bdcf10)

~~~json
{
  "source": "00bdcf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
