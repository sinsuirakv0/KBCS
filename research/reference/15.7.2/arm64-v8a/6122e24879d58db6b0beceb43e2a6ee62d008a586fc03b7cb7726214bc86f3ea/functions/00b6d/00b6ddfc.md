# 00b6ddfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6dec4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-e7ca8e1beb4f500cd906328435ef304f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6ddfc",
  "name": "_ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d095363187b126dc851e6a2e4eab0b71b83aba56f39f1fca2eb181271b3e712",
  "source_text_sha256": "0d095363187b126dc851e6a2e4eab0b71b83aba56f39f1fca2eb181271b3e712",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6ddfc",
        "00b6de3b"
      ]
    ],
    "bytes_sha256": "2b5bb2e28f07ce6980a36f434e1333ae2292ca99456494a58e15cbe1bd2ec685",
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
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 514 bytes

~~~c

long _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a19f8 == 0) {
                    /* catch() { ... } // from try @ 00b6ddb8 with catch @ 00b6de1c */
    DAT_010a19f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a19f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6ddfc"></a> `00b6ddfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6de00"></a> `00b6de00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6de04"></a> `00b6de04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6de08"></a> `00b6de08` | `b3 29 00 90` | adrp x19,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6de0c"></a> `00b6de0c` | `68 fe 44 f9` | ldr x8,[x19, #0x9f8] | `FALL_THROUGH`
<a id="insn-00b6de10"></a> `00b6de10` | `e8 00 00 b5` | cbnz x8,0x00b6de2c | `CONDITIONAL_JUMP`
<a id="insn-00b6de14"></a> `00b6de14` | `03 ba ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00b6de18"></a> `00b6de18` | `63 40 19 91` | add x3,x3,#0x650 | `FALL_THROUGH`
<a id="insn-00b6de1c"></a> `00b6de1c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b6de20"></a> `00b6de20` | `5c c0 01 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00b6de24"></a> `00b6de24` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b6de28"></a> `00b6de28` | `60 fe 04 f9` | str x0,[x19, #0x9f8] | `FALL_THROUGH`
<a id="insn-00b6de2c"></a> `00b6de2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6de30"></a> `00b6de30` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b6de34"></a> `00b6de34` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6de38"></a> `00b6de38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6ddfc`](#insn-00b6ddfc) 範囲 `[['00b6ddfc', '00b6de13']]`
  - `CONDITIONAL_JUMP` [`00b6de10`](#insn-00b6de10) → [`00b6de2c`](#insn-00b6de2c)
  - `FALL_THROUGH` [`00b6de10`](#insn-00b6de10) → [`00b6de14`](#insn-00b6de14)
- ブロック [`00b6de14`](#insn-00b6de14) 範囲 `[['00b6de14', '00b6de1b']]`
  - `FALL_THROUGH` [`00b6de18`](#insn-00b6de18) → [`00b6de1c`](#insn-00b6de1c)
- ブロック [`00b6de1c`](#insn-00b6de1c) 範囲 `[['00b6de1c', '00b6de2b']]`
  - `FALL_THROUGH` [`00b6de28`](#insn-00b6de28) → [`00b6de2c`](#insn-00b6de2c)
- ブロック [`00b6de2c`](#insn-00b6de2c) 範囲 `[['00b6de2c', '00b6de3b']]`

## 命令位置別の参照

- [`00b6ddfc`](#insn-00b6ddfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de00`](#insn-00b6de00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de0c`](#insn-00b6de0c) → `010a19f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6de10`](#insn-00b6de10) → [`00b6de2c`](#insn-00b6de2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de18`](#insn-00b6de18) → `002ad650`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6de20`](#insn-00b6de20) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00b6de28`](#insn-00b6de28) → `010a19f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6de2c`](#insn-00b6de2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6ddfc`](#insn-00b6ddfc)

~~~json
{
  "source": "00b6ddfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de00`](#insn-00b6de00)

~~~json
{
  "source": "00b6de00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de0c`](#insn-00b6de0c)

~~~json
{
  "source": "00b6de0c",
  "target": "010a19f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6de10`](#insn-00b6de10)

~~~json
{
  "source": "00b6de10",
  "target": "00b6de2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de18`](#insn-00b6de18)

~~~json
{
  "source": "00b6de18",
  "target": "002ad650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad64c",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ad64c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6de20`](#insn-00b6de20)

~~~json
{
  "source": "00b6de20",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6de28`](#insn-00b6de28)

~~~json
{
  "source": "00b6de28",
  "target": "010a19f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6de2c`](#insn-00b6de2c)

~~~json
{
  "source": "00b6de2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
