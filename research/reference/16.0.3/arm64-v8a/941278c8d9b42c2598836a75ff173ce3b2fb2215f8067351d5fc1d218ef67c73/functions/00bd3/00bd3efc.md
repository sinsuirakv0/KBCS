# 00bd3efc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd2f08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2f08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0083.md#compare-96e15ee8cb000e3891200a1828e19a2a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd3efc",
  "name": "_ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57c251a061ce5f05ac9938518959e2e5462ceae7a2ed4a40b536d935e3e37eda",
  "source_text_sha256": "57c251a061ce5f05ac9938518959e2e5462ceae7a2ed4a40b536d935e3e37eda",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd3efc",
        "00bd3f3b"
      ]
    ],
    "bytes_sha256": "f9e802bf6b45c952d52343d287e50fac5883c0462f7ea7f28f6016a6f62c420e",
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

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/FirebaseNetworkException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 446 bytes

~~~c

long _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_01127aa8 == 0) {
    DAT_01127aa8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01127aa8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd3efc"></a> `00bd3efc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd3f00"></a> `00bd3f00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3f04"></a> `00bd3f04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd3f08"></a> `00bd3f08` | `b3 2a 00 90` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd3f0c"></a> `00bd3f0c` | `68 56 45 f9` | ldr x8,[x19, #0xaa8] | `FALL_THROUGH`
<a id="insn-00bd3f10"></a> `00bd3f10` | `e8 00 00 b5` | cbnz x8,0x00bd3f2c | `CONDITIONAL_JUMP`
<a id="insn-00bd3f14"></a> `00bd3f14` | `63 b7 ff 90` | adrp x3,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bd3f18"></a> `00bd3f18` | `63 84 2b 91` | add x3,x3,#0xae1 | `FALL_THROUGH`
<a id="insn-00bd3f1c"></a> `00bd3f1c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd3f20"></a> `00bd3f20` | `24 20 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3f24"></a> `00bd3f24` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd3f28"></a> `00bd3f28` | `60 56 05 f9` | str x0,[x19, #0xaa8] | `FALL_THROUGH`
<a id="insn-00bd3f2c"></a> `00bd3f2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3f30"></a> `00bd3f30` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd3f34"></a> `00bd3f34` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd3f38"></a> `00bd3f38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd3efc`](#insn-00bd3efc) 範囲 `[['00bd3efc', '00bd3f13']]`
  - `CONDITIONAL_JUMP` [`00bd3f10`](#insn-00bd3f10) → [`00bd3f2c`](#insn-00bd3f2c)
  - `FALL_THROUGH` [`00bd3f10`](#insn-00bd3f10) → [`00bd3f14`](#insn-00bd3f14)
- ブロック [`00bd3f14`](#insn-00bd3f14) 範囲 `[['00bd3f14', '00bd3f2b']]`
  - `FALL_THROUGH` [`00bd3f28`](#insn-00bd3f28) → [`00bd3f2c`](#insn-00bd3f2c)
- ブロック [`00bd3f2c`](#insn-00bd3f2c) 範囲 `[['00bd3f2c', '00bd3f3b']]`

## 命令位置別の参照

- [`00bd3efc`](#insn-00bd3efc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f00`](#insn-00bd3f00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f0c`](#insn-00bd3f0c) → `01127aa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f10`](#insn-00bd3f10) → [`00bd3f2c`](#insn-00bd3f2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f18`](#insn-00bd3f18) → `002bfae1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd3f20`](#insn-00bd3f20) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f28`](#insn-00bd3f28) → `01127aa8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f2c`](#insn-00bd3f2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd3efc`](#insn-00bd3efc)

~~~json
{
  "source": "00bd3efc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f00`](#insn-00bd3f00)

~~~json
{
  "source": "00bd3f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f0c`](#insn-00bd3f0c)

~~~json
{
  "source": "00bd3f0c",
  "target": "01127aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127aa8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f10`](#insn-00bd3f10)

~~~json
{
  "source": "00bd3f10",
  "target": "00bd3f2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f18`](#insn-00bd3f18)

~~~json
{
  "source": "00bd3f18",
  "target": "002bfae1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfadd",
  "offset": 4,
  "size": 49,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002bfadd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd3f20`](#insn-00bd3f20)

~~~json
{
  "source": "00bd3f20",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3f28`](#insn-00bd3f28)

~~~json
{
  "source": "00bd3f28",
  "target": "01127aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127aa8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f2c`](#insn-00bd3f2c)

~~~json
{
  "source": "00bd3f2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
