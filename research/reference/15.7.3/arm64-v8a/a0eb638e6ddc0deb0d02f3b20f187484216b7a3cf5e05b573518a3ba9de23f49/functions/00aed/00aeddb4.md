# 00aeddb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aedcec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedcec.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-bfa90bc350ec7058078b725f4be187cb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeddf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeddf8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-a2a9ae4a2a45255a1c46828822685ccc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeddb4",
  "name": "_ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e0fc19171edaf972b5767a81087d33a8a873f5289b84b1bdb85f17c2e14a7ed",
  "source_text_sha256": "4e0fc19171edaf972b5767a81087d33a8a873f5289b84b1bdb85f17c2e14a7ed",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeddb4",
        "00aede53"
      ]
    ],
    "bytes_sha256": "23fa7290151cb9cfc9ff2e96be456cb7f2b30de2e7be0fa2e7182cb2bb6d1635",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0a20 != 0) {
    if (DAT_010a0a28 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0a28 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0a20);
    DAT_010a0a20 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeddb4"></a> `00aeddb4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeddb8"></a> `00aeddb8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeddbc"></a> `00aeddbc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeddc0"></a> `00aeddc0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeddc4"></a> `00aeddc4` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeddc8"></a> `00aeddc8` | `81 12 45 f9` | ldr x1,[x20, #0xa20] | `FALL_THROUGH`
<a id="insn-00aeddcc"></a> `00aeddcc` | `c1 03 00 b4` | cbz x1,0x00aede44 | `CONDITIONAL_JUMP`
<a id="insn-00aeddd0"></a> `00aeddd0` | `95 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeddd4"></a> `00aeddd4` | `a8 a2 68 39` | ldrb w8,[x21, #0xa28] | `FALL_THROUGH`
<a id="insn-00aeddd8"></a> `00aeddd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedddc"></a> `00aedddc` | `c8 00 00 34` | cbz w8,0x00aeddf4 | `CONDITIONAL_JUMP`
<a id="insn-00aedde0"></a> `00aedde0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedde4"></a> `00aedde4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedde8"></a> `00aedde8` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aeddec"></a> `00aeddec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeddf0"></a> `00aeddf0` | `bf a2 28 39` | strb wzr,[x21, #0xa28] | `FALL_THROUGH`
<a id="insn-00aeddf4"></a> `00aeddf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeddf8"></a> `00aeddf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeddfc"></a> `00aeddfc` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aede00"></a> `00aede00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede04"></a> `00aede04` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aede08"></a> `00aede08` | `20 01 00 54` | b.eq 0x00aede2c | `CONDITIONAL_JUMP`
<a id="insn-00aede0c"></a> `00aede0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede10"></a> `00aede10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede14"></a> `00aede14` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aede18"></a> `00aede18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede1c"></a> `00aede1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede20"></a> `00aede20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede24"></a> `00aede24` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aede28"></a> `00aede28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede2c"></a> `00aede2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede30"></a> `00aede30` | `81 12 45 f9` | ldr x1,[x20, #0xa20] | `FALL_THROUGH`
<a id="insn-00aede34"></a> `00aede34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede38"></a> `00aede38` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aede3c"></a> `00aede3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede40"></a> `00aede40` | `9f 12 05 f9` | str xzr,[x20, #0xa20] | `FALL_THROUGH`
<a id="insn-00aede44"></a> `00aede44` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aede48"></a> `00aede48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aede4c"></a> `00aede4c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aede50"></a> `00aede50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeddb4`](#insn-00aeddb4) 範囲 `[['00aeddb4', '00aeddcf']]`
  - `CONDITIONAL_JUMP` [`00aeddcc`](#insn-00aeddcc) → [`00aede44`](#insn-00aede44)
  - `FALL_THROUGH` [`00aeddcc`](#insn-00aeddcc) → [`00aeddd0`](#insn-00aeddd0)
- ブロック [`00aeddd0`](#insn-00aeddd0) 範囲 `[['00aeddd0', '00aedddf']]`
  - `CONDITIONAL_JUMP` [`00aedddc`](#insn-00aedddc) → [`00aeddf4`](#insn-00aeddf4)
  - `FALL_THROUGH` [`00aedddc`](#insn-00aedddc) → [`00aedde0`](#insn-00aedde0)
- ブロック [`00aedde0`](#insn-00aedde0) 範囲 `[['00aedde0', '00aeddf3']]`
  - `FALL_THROUGH` [`00aeddf0`](#insn-00aeddf0) → [`00aeddf4`](#insn-00aeddf4)
- ブロック [`00aeddf4`](#insn-00aeddf4) 範囲 `[['00aeddf4', '00aede0b']]`
  - `CONDITIONAL_JUMP` [`00aede08`](#insn-00aede08) → [`00aede2c`](#insn-00aede2c)
  - `FALL_THROUGH` [`00aede08`](#insn-00aede08) → [`00aede0c`](#insn-00aede0c)
- ブロック [`00aede0c`](#insn-00aede0c) 範囲 `[['00aede0c', '00aede2b']]`
  - `FALL_THROUGH` [`00aede28`](#insn-00aede28) → [`00aede2c`](#insn-00aede2c)
- ブロック [`00aede2c`](#insn-00aede2c) 範囲 `[['00aede2c', '00aede43']]`
  - `FALL_THROUGH` [`00aede40`](#insn-00aede40) → [`00aede44`](#insn-00aede44)
- ブロック [`00aede44`](#insn-00aede44) 範囲 `[['00aede44', '00aede53']]`

## 命令位置別の参照

- [`00aeddb4`](#insn-00aeddb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddb8`](#insn-00aeddb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddbc`](#insn-00aeddbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddc8`](#insn-00aeddc8) → `010a0a20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeddcc`](#insn-00aeddcc) → [`00aede44`](#insn-00aede44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddd4`](#insn-00aeddd4) → `010a0a28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aedddc`](#insn-00aedddc) → [`00aeddf4`](#insn-00aeddf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddf0`](#insn-00aeddf0) → `010a0a28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aede08`](#insn-00aede08) → [`00aede2c`](#insn-00aede2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede30`](#insn-00aede30) → `010a0a20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aede40`](#insn-00aede40) → `010a0a20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aede44`](#insn-00aede44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede48`](#insn-00aede48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeddb4`](#insn-00aeddb4)

~~~json
{
  "source": "00aeddb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddb8`](#insn-00aeddb8)

~~~json
{
  "source": "00aeddb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddbc`](#insn-00aeddbc)

~~~json
{
  "source": "00aeddbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddc8`](#insn-00aeddc8)

~~~json
{
  "source": "00aeddc8",
  "target": "010a0a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeddcc`](#insn-00aeddcc)

~~~json
{
  "source": "00aeddcc",
  "target": "00aede44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddd4`](#insn-00aeddd4)

~~~json
{
  "source": "00aeddd4",
  "target": "010a0a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a28",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedddc`](#insn-00aedddc)

~~~json
{
  "source": "00aedddc",
  "target": "00aeddf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddf0`](#insn-00aeddf0)

~~~json
{
  "source": "00aeddf0",
  "target": "010a0a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a28",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede08`](#insn-00aede08)

~~~json
{
  "source": "00aede08",
  "target": "00aede2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede30`](#insn-00aede30)

~~~json
{
  "source": "00aede30",
  "target": "010a0a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede40`](#insn-00aede40)

~~~json
{
  "source": "00aede40",
  "target": "010a0a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede44`](#insn-00aede44)

~~~json
{
  "source": "00aede44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede48`](#insn-00aede48)

~~~json
{
  "source": "00aede48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
