# 00aea0fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aea1c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea1c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-a177cc47e8ac24e510b04c9f509bdca6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea0fc",
  "name": "_ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fb6f9242c5ff129b1fc069af1e1c3a7c8596962991e998d12f5f5d23d695e85",
  "source_text_sha256": "5fb6f9242c5ff129b1fc069af1e1c3a7c8596962991e998d12f5f5d23d695e85",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea0fc",
        "00aea13b"
      ]
    ],
    "bytes_sha256": "67f36a353664509240f1c62c98e31198844cf87e4528f92c4c51fb7d03228903",
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
"java/lang/Enum"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 430 bytes

~~~c

long _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a06a8 == 0) {
    DAT_010a06a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a06a8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea0fc"></a> `00aea0fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aea100"></a> `00aea100` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea104"></a> `00aea104` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aea108"></a> `00aea108` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea10c"></a> `00aea10c` | `68 56 43 f9` | ldr x8,[x19, #0x6a8] | `FALL_THROUGH`
<a id="insn-00aea110"></a> `00aea110` | `e8 00 00 b5` | cbnz x8,0x00aea12c | `CONDITIONAL_JUMP`
<a id="insn-00aea114"></a> `00aea114` | `23 be ff d0` | adrp x3,0x2b0000 | `FALL_THROUGH`
<a id="insn-00aea118"></a> `00aea118` | `63 ec 12 91` | add x3,x3,#0x4bb | `FALL_THROUGH`
<a id="insn-00aea11c"></a> `00aea11c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aea120"></a> `00aea120` | `9c cf 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aea124"></a> `00aea124` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aea128"></a> `00aea128` | `60 56 03 f9` | str x0,[x19, #0x6a8] | `FALL_THROUGH`
<a id="insn-00aea12c"></a> `00aea12c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea130"></a> `00aea130` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aea134"></a> `00aea134` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aea138"></a> `00aea138` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea0fc`](#insn-00aea0fc) 範囲 `[['00aea0fc', '00aea113']]`
  - `CONDITIONAL_JUMP` [`00aea110`](#insn-00aea110) → [`00aea12c`](#insn-00aea12c)
  - `FALL_THROUGH` [`00aea110`](#insn-00aea110) → [`00aea114`](#insn-00aea114)
- ブロック [`00aea114`](#insn-00aea114) 範囲 `[['00aea114', '00aea12b']]`
  - `FALL_THROUGH` [`00aea128`](#insn-00aea128) → [`00aea12c`](#insn-00aea12c)
- ブロック [`00aea12c`](#insn-00aea12c) 範囲 `[['00aea12c', '00aea13b']]`

## 命令位置別の参照

- [`00aea0fc`](#insn-00aea0fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea100`](#insn-00aea100) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea10c`](#insn-00aea10c) → `010a06a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea110`](#insn-00aea110) → [`00aea12c`](#insn-00aea12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea118`](#insn-00aea118) → `002b04bb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aea120`](#insn-00aea120) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aea128`](#insn-00aea128) → `010a06a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea12c`](#insn-00aea12c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea0fc`](#insn-00aea0fc)

~~~json
{
  "source": "00aea0fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea100`](#insn-00aea100)

~~~json
{
  "source": "00aea100",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea10c`](#insn-00aea10c)

~~~json
{
  "source": "00aea10c",
  "target": "010a06a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a06a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea110`](#insn-00aea110)

~~~json
{
  "source": "00aea110",
  "target": "00aea12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea118`](#insn-00aea118)

~~~json
{
  "source": "00aea118",
  "target": "002b04bb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b04bb",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f456e756d00",
  "capture_start": "002b04bb",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea120`](#insn-00aea120)

~~~json
{
  "source": "00aea120",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea128`](#insn-00aea128)

~~~json
{
  "source": "00aea128",
  "target": "010a06a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a06a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea12c`](#insn-00aea12c)

~~~json
{
  "source": "00aea12c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
