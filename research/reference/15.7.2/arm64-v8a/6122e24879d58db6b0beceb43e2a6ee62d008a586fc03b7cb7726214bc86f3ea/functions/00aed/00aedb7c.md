# 00aedb7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedc44`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-9da4ad1e589b66d5e3abb9d81c1a7ae4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedb7c",
  "name": "_ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35085ed03aa4b67810327acc63a9f69dd42603b1f786aa21f88874405864aef8",
  "source_text_sha256": "35085ed03aa4b67810327acc63a9f69dd42603b1f786aa21f88874405864aef8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedb7c",
        "00aedbbb"
      ]
    ],
    "bytes_sha256": "61feee2ace2f5b223818ed47e518fecd505a0605883737b9c5a8537aff364301",
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

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 422 bytes

~~~c

long _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0960 == 0) {
    DAT_010a0960 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0960;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedb7c"></a> `00aedb7c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedb80"></a> `00aedb80` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedb84"></a> `00aedb84` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedb88"></a> `00aedb88` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedb8c"></a> `00aedb8c` | `68 b2 44 f9` | ldr x8,[x19, #0x960] | `FALL_THROUGH`
<a id="insn-00aedb90"></a> `00aedb90` | `e8 00 00 b5` | cbnz x8,0x00aedbac | `CONDITIONAL_JUMP`
<a id="insn-00aedb94"></a> `00aedb94` | `43 bd ff d0` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aedb98"></a> `00aedb98` | `63 e0 13 91` | add x3,x3,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aedb9c"></a> `00aedb9c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedba0"></a> `00aedba0` | `fc c0 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aedba4"></a> `00aedba4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedba8"></a> `00aedba8` | `60 b2 04 f9` | str x0,[x19, #0x960] | `FALL_THROUGH`
<a id="insn-00aedbac"></a> `00aedbac` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedbb0"></a> `00aedbb0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedbb4"></a> `00aedbb4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedbb8"></a> `00aedbb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedb7c`](#insn-00aedb7c) 範囲 `[['00aedb7c', '00aedb93']]`
  - `CONDITIONAL_JUMP` [`00aedb90`](#insn-00aedb90) → [`00aedbac`](#insn-00aedbac)
  - `FALL_THROUGH` [`00aedb90`](#insn-00aedb90) → [`00aedb94`](#insn-00aedb94)
- ブロック [`00aedb94`](#insn-00aedb94) 範囲 `[['00aedb94', '00aedbab']]`
  - `FALL_THROUGH` [`00aedba8`](#insn-00aedba8) → [`00aedbac`](#insn-00aedbac)
- ブロック [`00aedbac`](#insn-00aedbac) 範囲 `[['00aedbac', '00aedbbb']]`

## 命令位置別の参照

- [`00aedb7c`](#insn-00aedb7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb80`](#insn-00aedb80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb8c`](#insn-00aedb8c) → `010a0960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedb90`](#insn-00aedb90) → [`00aedbac`](#insn-00aedbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb98`](#insn-00aedb98) → `002974f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedba0`](#insn-00aedba0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aedba8`](#insn-00aedba8) → `010a0960`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedbac`](#insn-00aedbac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedb7c`](#insn-00aedb7c)

~~~json
{
  "source": "00aedb7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb80`](#insn-00aedb80)

~~~json
{
  "source": "00aedb80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb8c`](#insn-00aedb8c)

~~~json
{
  "source": "00aedb8c",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedb90`](#insn-00aedb90)

~~~json
{
  "source": "00aedb90",
  "target": "00aedbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb98`](#insn-00aedb98)

~~~json
{
  "source": "00aedb98",
  "target": "002974f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974f8",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "002974f8",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedba0`](#insn-00aedba0)

~~~json
{
  "source": "00aedba0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedba8`](#insn-00aedba8)

~~~json
{
  "source": "00aedba8",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedbac`](#insn-00aedbac)

~~~json
{
  "source": "00aedbac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
