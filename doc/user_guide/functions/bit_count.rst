.. _bit_count:

BIT_COUNT
=========

``BIT_COUNT`` counts the bits set to ``1`` in the 64-bit integer value produced from an integer-valued input.

Syntax
------

.. code-block:: sql

   BIT_COUNT(n)

DESCRIPTION
-----------

================== ================= ====================
Parameter / Return Type              Range
================== ================= ====================
``n``              ``DECIMAL(36,0)`` Integer-valued input
Return             ``DECIMAL(2,0)``  ``0`` to ``64``
================== ================= ====================

The function returns the number of set bits in ``n``.

Values above ``18446744073709551615`` saturate to that maximum, values below ``-9223372036854775808`` saturate to that minimum, and bits above the 64-bit range are ignored.

Given an integer-valued input, the fractional part is ignored.

Negative values are interpreted using a 64-bit two's-complement representation.

``NULL`` input returns ``NULL``.

Examples
--------

.. code-block:: sql

   SELECT BIT_COUNT(NULL);

Returns ``NULL``.

.. code-block:: sql

   SELECT BIT_COUNT(0);

Returns ``0`` because no bits are set.

.. code-block:: sql

   SELECT BIT_COUNT(29);

Returns ``4`` because ``29`` is ``11101`` in binary.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(29 AS DECIMAL(18,0)));

Returns ``4``.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(3.1414 AS DECIMAL(18,4)));

Returns ``2``. The input is converted to the function's integer-valued parameter.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(29.5 AS DOUBLE));

Returns ``4``.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(1099512676383 AS DECIMAL(36,0)));

Returns ``9``.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(18446744073709551616 AS DECIMAL(36,0)));

Returns ``64``.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(-999999999999999999999999999999999999 AS DECIMAL(36,0)));

Returns ``1``.
