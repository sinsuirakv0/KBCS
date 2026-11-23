# 00aeda0c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aed944`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed944.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-d7b52054aca8f2f9638df0d6b4678ab2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeda50`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeda50.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-53fcdfa7d13ca2f9e32c4b691784e964)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeda0c",
  "name": "_ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "678e9ecf9339e47d9a462a758a3513d43f0277178405c2db2d828129e2428fb4",
  "source_text_sha256": "678e9ecf9339e47d9a462a758a3513d43f0277178405c2db2d828129e2428fb4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeda0c",
        "00aedaab"
      ]
    ],
    "bytes_sha256": "ac1e630bc29a4c03120d8771f6e4e0ddfadaab4adfcab164d9516d13f61c562a",
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

## 疑似コード / UTF-8 509 bytes

~~~c

void _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a09f0 != 0) {
    if (DAT_010a09f8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a09f8 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a09f0);
    DAT_010a09f0 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeda0c"></a> `00aeda0c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeda10"></a> `00aeda10` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeda14"></a> `00aeda14` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeda18"></a> `00aeda18` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeda1c"></a> `00aeda1c` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeda20"></a> `00aeda20` | `81 fa 44 f9` | ldr x1,[x20, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aeda24"></a> `00aeda24` | `c1 03 00 b4` | cbz x1,0x00aeda9c | `CONDITIONAL_JUMP`
<a id="insn-00aeda28"></a> `00aeda28` | `95 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeda2c"></a> `00aeda2c` | `a8 e2 67 39` | ldrb w8,[x21, #0x9f8] | `FALL_THROUGH`
<a id="insn-00aeda30"></a> `00aeda30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeda34"></a> `00aeda34` | `c8 00 00 34` | cbz w8,0x00aeda4c | `CONDITIONAL_JUMP`
<a id="insn-00aeda38"></a> `00aeda38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeda3c"></a> `00aeda3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeda40"></a> `00aeda40` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aeda44"></a> `00aeda44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeda48"></a> `00aeda48` | `bf e2 27 39` | strb wzr,[x21, #0x9f8] | `FALL_THROUGH`
<a id="insn-00aeda4c"></a> `00aeda4c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeda50"></a> `00aeda50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeda54"></a> `00aeda54` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeda58"></a> `00aeda58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeda5c"></a> `00aeda5c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeda60"></a> `00aeda60` | `20 01 00 54` | b.eq 0x00aeda84 | `CONDITIONAL_JUMP`
<a id="insn-00aeda64"></a> `00aeda64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeda68"></a> `00aeda68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeda6c"></a> `00aeda6c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeda70"></a> `00aeda70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeda74"></a> `00aeda74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeda78"></a> `00aeda78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeda7c"></a> `00aeda7c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeda80"></a> `00aeda80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeda84"></a> `00aeda84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeda88"></a> `00aeda88` | `81 fa 44 f9` | ldr x1,[x20, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aeda8c"></a> `00aeda8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeda90"></a> `00aeda90` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aeda94"></a> `00aeda94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeda98"></a> `00aeda98` | `9f fa 04 f9` | str xzr,[x20, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aeda9c"></a> `00aeda9c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aedaa0"></a> `00aedaa0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedaa4"></a> `00aedaa4` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aedaa8"></a> `00aedaa8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeda0c`](#insn-00aeda0c) 範囲 `[['00aeda0c', '00aeda27']]`
  - `CONDITIONAL_JUMP` [`00aeda24`](#insn-00aeda24) → [`00aeda9c`](#insn-00aeda9c)
  - `FALL_THROUGH` [`00aeda24`](#insn-00aeda24) → [`00aeda28`](#insn-00aeda28)
- ブロック [`00aeda28`](#insn-00aeda28) 範囲 `[['00aeda28', '00aeda37']]`
  - `CONDITIONAL_JUMP` [`00aeda34`](#insn-00aeda34) → [`00aeda4c`](#insn-00aeda4c)
  - `FALL_THROUGH` [`00aeda34`](#insn-00aeda34) → [`00aeda38`](#insn-00aeda38)
- ブロック [`00aeda38`](#insn-00aeda38) 範囲 `[['00aeda38', '00aeda4b']]`
  - `FALL_THROUGH` [`00aeda48`](#insn-00aeda48) → [`00aeda4c`](#insn-00aeda4c)
- ブロック [`00aeda4c`](#insn-00aeda4c) 範囲 `[['00aeda4c', '00aeda63']]`
  - `CONDITIONAL_JUMP` [`00aeda60`](#insn-00aeda60) → [`00aeda84`](#insn-00aeda84)
  - `FALL_THROUGH` [`00aeda60`](#insn-00aeda60) → [`00aeda64`](#insn-00aeda64)
- ブロック [`00aeda64`](#insn-00aeda64) 範囲 `[['00aeda64', '00aeda83']]`
  - `FALL_THROUGH` [`00aeda80`](#insn-00aeda80) → [`00aeda84`](#insn-00aeda84)
- ブロック [`00aeda84`](#insn-00aeda84) 範囲 `[['00aeda84', '00aeda9b']]`
  - `FALL_THROUGH` [`00aeda98`](#insn-00aeda98) → [`00aeda9c`](#insn-00aeda9c)
- ブロック [`00aeda9c`](#insn-00aeda9c) 範囲 `[['00aeda9c', '00aedaab']]`

## 命令位置別の参照

- [`00aeda0c`](#insn-00aeda0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda10`](#insn-00aeda10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda14`](#insn-00aeda14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda20`](#insn-00aeda20) → `010a09f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeda24`](#insn-00aeda24) → [`00aeda9c`](#insn-00aeda9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda2c`](#insn-00aeda2c) → `010a09f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeda34`](#insn-00aeda34) → [`00aeda4c`](#insn-00aeda4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda48`](#insn-00aeda48) → `010a09f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeda60`](#insn-00aeda60) → [`00aeda84`](#insn-00aeda84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda88`](#insn-00aeda88) → `010a09f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeda98`](#insn-00aeda98) → `010a09f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeda9c`](#insn-00aeda9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedaa0`](#insn-00aedaa0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeda0c`](#insn-00aeda0c)

~~~json
{
  "source": "00aeda0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda10`](#insn-00aeda10)

~~~json
{
  "source": "00aeda10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda14`](#insn-00aeda14)

~~~json
{
  "source": "00aeda14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda20`](#insn-00aeda20)

~~~json
{
  "source": "00aeda20",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeda24`](#insn-00aeda24)

~~~json
{
  "source": "00aeda24",
  "target": "00aeda9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda2c`](#insn-00aeda2c)

~~~json
{
  "source": "00aeda2c",
  "target": "010a09f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeda34`](#insn-00aeda34)

~~~json
{
  "source": "00aeda34",
  "target": "00aeda4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda48`](#insn-00aeda48)

~~~json
{
  "source": "00aeda48",
  "target": "010a09f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeda60`](#insn-00aeda60)

~~~json
{
  "source": "00aeda60",
  "target": "00aeda84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda88`](#insn-00aeda88)

~~~json
{
  "source": "00aeda88",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeda98`](#insn-00aeda98)

~~~json
{
  "source": "00aeda98",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeda9c`](#insn-00aeda9c)

~~~json
{
  "source": "00aeda9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedaa0`](#insn-00aedaa0)

~~~json
{
  "source": "00aedaa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
