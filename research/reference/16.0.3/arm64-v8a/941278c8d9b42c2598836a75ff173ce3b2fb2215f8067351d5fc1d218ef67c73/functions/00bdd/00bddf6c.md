# 00bddf6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcf78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-32d212ddfaf3de30c2d91309b91789b8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddf6c",
  "name": "_ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fcd3fb20ee451b6f1f1a04e3c0b04c173889e6b8726da4dd36477e8504ea17e",
  "source_text_sha256": "8fcd3fb20ee451b6f1f1a04e3c0b04c173889e6b8726da4dd36477e8504ea17e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddf6c",
        "00bddfaf"
      ]
    ],
    "bytes_sha256": "f8859d2df833978eb390b664d243d1c0cbc2c4857736e6888bc7f55ab2550333",
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

- [00c5bfb0](../00c5b/00c5bfb0.md)

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
  if (DAT_01127dc0 == 0) {
    DAT_01127dc0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  return DAT_01127dc0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddf6c"></a> `00bddf6c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddf70"></a> `00bddf70` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf74"></a> `00bddf74` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddf78"></a> `00bddf78` | `53 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bddf7c"></a> `00bddf7c` | `68 e2 46 f9` | ldr x8,[x19, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bddf80"></a> `00bddf80` | `08 01 00 b5` | cbnz x8,0x00bddfa0 | `CONDITIONAL_JUMP`
<a id="insn-00bddf84"></a> `00bddf84` | `e3 b6 ff f0` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bddf88"></a> `00bddf88` | `63 68 0b 91` | add x3,x3,#0x2da | `FALL_THROUGH`
<a id="insn-00bddf8c"></a> `00bddf8c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddf90"></a> `00bddf90` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddf94"></a> `00bddf94` | `07 f8 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddf98"></a> `00bddf98` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bddf9c"></a> `00bddf9c` | `60 e2 06 f9` | str x0,[x19, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bddfa0"></a> `00bddfa0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddfa4"></a> `00bddfa4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bddfa8"></a> `00bddfa8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddfac"></a> `00bddfac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddf6c`](#insn-00bddf6c) 範囲 `[['00bddf6c', '00bddf83']]`
  - `CONDITIONAL_JUMP` [`00bddf80`](#insn-00bddf80) → [`00bddfa0`](#insn-00bddfa0)
  - `FALL_THROUGH` [`00bddf80`](#insn-00bddf80) → [`00bddf84`](#insn-00bddf84)
- ブロック [`00bddf84`](#insn-00bddf84) 範囲 `[['00bddf84', '00bddf9f']]`
  - `FALL_THROUGH` [`00bddf9c`](#insn-00bddf9c) → [`00bddfa0`](#insn-00bddfa0)
- ブロック [`00bddfa0`](#insn-00bddfa0) 範囲 `[['00bddfa0', '00bddfaf']]`

## 命令位置別の参照

- [`00bddf6c`](#insn-00bddf6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf70`](#insn-00bddf70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf7c`](#insn-00bddf7c) → `01127dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddf80`](#insn-00bddf80) → [`00bddfa0`](#insn-00bddfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf88`](#insn-00bddf88) → `002bc2da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddf94`](#insn-00bddf94) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bddf9c`](#insn-00bddf9c) → `01127dc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddfa0`](#insn-00bddfa0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddf6c`](#insn-00bddf6c)

~~~json
{
  "source": "00bddf6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf70`](#insn-00bddf70)

~~~json
{
  "source": "00bddf70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf7c`](#insn-00bddf7c)

~~~json
{
  "source": "00bddf7c",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddf80`](#insn-00bddf80)

~~~json
{
  "source": "00bddf80",
  "target": "00bddfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf88`](#insn-00bddf88)

~~~json
{
  "source": "00bddf88",
  "target": "002bc2da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc2d6",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc2d6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddf94`](#insn-00bddf94)

~~~json
{
  "source": "00bddf94",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddf9c`](#insn-00bddf9c)

~~~json
{
  "source": "00bddf9c",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddfa0`](#insn-00bddfa0)

~~~json
{
  "source": "00bddfa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
