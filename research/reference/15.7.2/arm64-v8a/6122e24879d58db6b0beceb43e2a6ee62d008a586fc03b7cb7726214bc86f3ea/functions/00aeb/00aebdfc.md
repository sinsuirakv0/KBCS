# 00aebdfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebec4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebec4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-866755f86d2235d45bb96c497792dfc1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebdfc",
  "name": "_ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f3506b4fd324c934b3dbb347da2805456979fdd25d2b3b4b9b1f06b4728a2f7",
  "source_text_sha256": "7f3506b4fd324c934b3dbb347da2805456979fdd25d2b3b4b9b1f06b4728a2f7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebdfc",
        "00aebe3b"
      ]
    ],
    "bytes_sha256": "662b9cf63d0683900488445ae7a0bf0fb0ab1f156a704cd59385837bc5b302c3",
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
"java/util/List"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 446 bytes

~~~c

long _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0820 == 0) {
    DAT_010a0820 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0820;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebdfc"></a> `00aebdfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebe00"></a> `00aebe00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe04"></a> `00aebe04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebe08"></a> `00aebe08` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebe0c"></a> `00aebe0c` | `68 12 44 f9` | ldr x8,[x19, #0x820] | `FALL_THROUGH`
<a id="insn-00aebe10"></a> `00aebe10` | `e8 00 00 b5` | cbnz x8,0x00aebe2c | `CONDITIONAL_JUMP`
<a id="insn-00aebe14"></a> `00aebe14` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aebe18"></a> `00aebe18` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aebe1c"></a> `00aebe1c` | `63 14 0e 91` | add x3,x3,#0x385 | `FALL_THROUGH`
<a id="insn-00aebe20"></a> `00aebe20` | `5c c8 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe24"></a> `00aebe24` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebe28"></a> `00aebe28` | `60 12 04 f9` | str x0,[x19, #0x820] | `FALL_THROUGH`
<a id="insn-00aebe2c"></a> `00aebe2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe30"></a> `00aebe30` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebe34"></a> `00aebe34` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebe38"></a> `00aebe38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebdfc`](#insn-00aebdfc) 範囲 `[['00aebdfc', '00aebe13']]`
  - `CONDITIONAL_JUMP` [`00aebe10`](#insn-00aebe10) → [`00aebe2c`](#insn-00aebe2c)
  - `FALL_THROUGH` [`00aebe10`](#insn-00aebe10) → [`00aebe14`](#insn-00aebe14)
- ブロック [`00aebe14`](#insn-00aebe14) 範囲 `[['00aebe14', '00aebe2b']]`
  - `FALL_THROUGH` [`00aebe28`](#insn-00aebe28) → [`00aebe2c`](#insn-00aebe2c)
- ブロック [`00aebe2c`](#insn-00aebe2c) 範囲 `[['00aebe2c', '00aebe3b']]`

## 命令位置別の参照

- [`00aebdfc`](#insn-00aebdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe00`](#insn-00aebe00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe0c`](#insn-00aebe0c) → `010a0820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebe10`](#insn-00aebe10) → [`00aebe2c`](#insn-00aebe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe1c`](#insn-00aebe1c) → `00290385`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebe20`](#insn-00aebe20) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aebe28`](#insn-00aebe28) → `010a0820`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebe2c`](#insn-00aebe2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebdfc`](#insn-00aebdfc)

~~~json
{
  "source": "00aebdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe00`](#insn-00aebe00)

~~~json
{
  "source": "00aebe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe0c`](#insn-00aebe0c)

~~~json
{
  "source": "00aebe0c",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebe10`](#insn-00aebe10)

~~~json
{
  "source": "00aebe10",
  "target": "00aebe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe1c`](#insn-00aebe1c)

~~~json
{
  "source": "00aebe1c",
  "target": "00290385",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290385",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4c69737400",
  "capture_start": "00290385",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebe20`](#insn-00aebe20)

~~~json
{
  "source": "00aebe20",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe28`](#insn-00aebe28)

~~~json
{
  "source": "00aebe28",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebe2c`](#insn-00aebe2c)

~~~json
{
  "source": "00aebe2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
